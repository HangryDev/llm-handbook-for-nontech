#!/usr/bin/env python3
"""
Case Study News Generator - RSS 피드 기반 뉴스 다이제스트 생성
4개 카테고리별로 최신 뉴스를 수집하여 마크다운 생성
"""

import os
import re
import requests
import feedparser
from datetime import datetime
from collections import defaultdict
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# RSS Feed Configuration by Category
FEED_CONFIG = {
    "practical": {
        "title": "🛠️ Practical (Prompt, Agent, MCP)",
        "color": "#3498db",
        "feeds": [
            {"name": "Latent Space", "url": "https://latent.space/feed", "count": 3, "badge_color": "#8e44ad"},
            {"name": "Ahead of AI", "url": "https://magazine.sebastianraschka.com/feed", "count": 3, "badge_color": "#2c3e50"},
            {"name": "Anthropic News", "url": "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_news.xml", "count": 3, "badge_color": "#d35400"},
            {"name": "Dev.to AI", "url": "https://dev.to/feed/tag/ai", "count": 5, "badge_color": "#000000"},
        ]
    },
    "business": {
        "title": "💼 Business Cases",
        "color": "#e67e22",
        "feeds": [
            {"name": "Harvard Business Review", "url": "http://feeds.hbr.org/harvardbusiness", "count": 3, "badge_color": "#c0392b"},
            {"name": "The Sequence", "url": "https://thesequence.substack.com/feed", "count": 3, "badge_color": "#27ae60"},
        ]
    },
    "big_tech": {
        "title": "🏢 Big Tech News",
        "color": "#e74c3c",
        "feeds": [
            {"name": "OpenAI Blog", "url": "https://openai.com/blog/rss.xml", "count": 3, "badge_color": "#10a37f"},
            {"name": "Google AI Blog", "url": "http://googleaiblog.blogspot.com/atom.xml", "count": 3, "badge_color": "#4285f4"},
        ]
    },
    "insights": {
        "title": "💡 Insights (General)",
        "color": "#27ae60",
        "feeds": [
            {"name": "MIT Technology Review", "url": "https://www.technologyreview.com/feed/", "count": 3, "badge_color": "#000000"},
            {"name": "Ben's Bites", "url": "https://www.bensbites.com/feed", "count": 3, "badge_color": "#16a085"},
        ]
    }
}


def clean_html(text):
    """HTML 태그를 완전히 제거하고 텍스트만 추출"""
    if not text:
        return ""

    # BeautifulSoup으로 HTML 파싱 및 태그 제거
    soup = BeautifulSoup(text, 'html.parser')

    # 모든 script, style 태그 제거
    for script in soup(["script", "style"]):
        script.decompose()

    # 텍스트만 추출
    text = soup.get_text(separator=' ', strip=True)

    # HTML 엔티티 디코드 및 특수문자 정리
    text = re.sub(r'&#\d+;', '', text)
    text = re.sub(r'&[a-z]+;', '', text)

    # 연속된 공백을 하나로
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def is_korean_or_english(text):
    """텍스트가 한글 또는 영어인지 확인 (아랍어 등 필터링)"""
    if not text:
        return False

    # 영어, 한글, 숫자, 기본 특수문자만 허용
    allowed_pattern = re.compile(r'^[a-zA-Z0-9가-힣\s\.\,\!\?\-\:\;\(\)\'\"\&\/\+\%\$\#\@]*$')

    # 아랍어, 힌디어 등 다른 스크립트 문자 검출
    arabic_hindi_pattern = re.compile(r'[\u0600-\u06FF\u0900-\u097F]')

    # 아랍어/힌디어 등이 포함되어 있으면 False
    if arabic_hindi_pattern.search(text):
        return False

    # 허용된 문자만 있는지 확인 (최소 70% 이상)
    clean_chars = len(re.findall(r'[a-zA-Z0-9가-힣]', text))
    total_chars = len(text.replace(' ', ''))

    if total_chars == 0:
        return False

    return clean_chars / total_chars > 0.7


def translate_to_korean(text, max_length=5000):
    """영어 텍스트를 한글로 번역"""
    if not text or len(text.strip()) == 0:
        return text

    try:
        # 텍스트가 이미 한글인지 확인
        korean_chars = len(re.findall(r'[가-힣]', text))
        if korean_chars > len(text) * 0.3:  # 30% 이상 한글이면 번역하지 않음
            return text

        # 길이 제한
        if len(text) > max_length:
            text = text[:max_length]

        translator = GoogleTranslator(source='auto', target='ko')
        translated = translator.translate(text)
        return translated
    except Exception as e:
        print(f"  ⚠️  Translation error: {str(e)[:50]}")
        return text


def fetch_feed(feed_url, count=3):
    """RSS 피드에서 최신 뉴스 가져오기"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/rss+xml, application/xml, text/xml, */*',
        }

        response = requests.get(feed_url, headers=headers, timeout=30)
        response.raise_for_status()

        feed = feedparser.parse(response.content)

        articles = []
        for entry in feed.entries[:count * 2]:  # 필터링을 고려해서 더 많이 가져옴
            # 제목 검증 - 아랍어 등 필터링
            if not is_korean_or_english(entry.title):
                print(f"  ⏭️  Skipped non-Korean/English title: {entry.title[:50]}")
                continue

            # 날짜 파싱
            pub_date = None
            if hasattr(entry, 'published_parsed') and entry.published_parsed:
                pub_date = datetime(*entry.published_parsed[:6])
            elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                pub_date = datetime(*entry.updated_parsed[:6])
            else:
                pub_date = datetime.now()

            # 요약 추출 및 정리
            summary = ""
            if hasattr(entry, 'summary'):
                summary = clean_html(entry.summary)
            elif hasattr(entry, 'description'):
                summary = clean_html(entry.description)

            # 요약도 검증
            if summary and not is_korean_or_english(summary):
                summary = ""

            # 요약 길이 제한
            if len(summary) > 200:
                summary = summary[:200] + "..."

            # 제목과 요약 번역
            title_ko = translate_to_korean(entry.title)
            summary_ko = translate_to_korean(summary) if summary else ""

            articles.append({
                'title': title_ko,
                'url': entry.link,
                'date': pub_date,
                'summary': summary_ko
            })

            # 원하는 개수만큼 수집되면 종료
            if len(articles) >= count:
                break

        return articles

    except Exception as e:
        print(f"⚠️  Error fetching {feed_url}: {str(e)}")
        return []


def generate_full_markdown_for_category(category_id, category_data, source_articles_map):
    """
    Generate complete markdown file content for a single category using list layout.
    source_articles_map: { 'FeedName': [article1, article2...], ... }
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    category_title = category_data['title']

    md_content = f"""# {category_title}

*Last Updated: {current_date}*

---

"""
    
    all_articles = []
    for source_name, articles in source_articles_map.items():
        # Find font color
        feed_color = "#6c757d"
        for feed in category_data['feeds']:
            if feed['name'] == source_name:
                feed_color = feed.get('badge_color', "#6c757d")
                break
        
        for article in articles:
            article['source_name'] = source_name
            article['feed_color'] = feed_color
            all_articles.append(article)
    
    # Sort by date descending
    all_articles.sort(key=lambda x: x['date'], reverse=True)

    for article in all_articles:
        # content preparation
        title = article['title'].replace('"', '\\"').replace('[', '\\[').replace(']', '\\]')
        summary = article['summary'].replace('\n', ' ').strip()
        url = article['url']
        source_name = article['source_name']
        feed_color = article['feed_color']
        
        # Simple list format with colored source badge
        md_content += f"- <span style='background-color: {feed_color}; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.8em; font-weight: bold;'>{source_name}</span> **[{title}]({url})** - {summary}\n\n"

    # Add Footer
    md_content += """
---
*Generated by [LLM Handbook News Digest](https://github.com/springCoolers/llm-handbook)*
"""
    return md_content


def main():
    """메인 실행 함수"""
    print("=" * 60)
    print("Case Study News Digest Generator")
    print("=" * 60)

    news_by_category = defaultdict(dict)
    total_articles = 0

    # 카테고리별로 RSS 피드 수집
    for category_id, category_data in FEED_CONFIG.items():
        print(f"\\n📂 Processing category: {category_data['title']}")

        for feed_config in category_data['feeds']:
            feed_name = feed_config['name']
            feed_url = feed_config['url']
            count = feed_config['count']

            print(f"  📰 Fetching {feed_name}...")
            articles = fetch_feed(feed_url, count)

            if articles:
                news_by_category[category_id][feed_name] = articles
                total_articles += len(articles)
                print(f"     ✅ {len(articles)} articles collected")
            else:
                print(f"     ⚠️  No articles found")

    print(f"\\n{'=' * 60}")
    print(f"✅ Total: {total_articles} articles collected")
    print(f"{'=' * 60}\\n")

    # 마크다운 파일 생성 (sections 폴더)
    sections_dir = "/home/robert/work/llm_knowledge_foundation/llm-handbook/_contents/llm-engineering/news/case-study/sections"
    if not os.path.exists(sections_dir):
        os.makedirs(sections_dir)
        print(f"📂 Created directory: {sections_dir}")

    # File mapping
    file_mapping = {
        "practical": "practical.md",
        "business": "business-cases.md",
        "big_tech": "bigtech.md",
        "insights": "insight.md"
    }

    print("📝 Generating markdown files...")

    for category_id, category_data in FEED_CONFIG.items():
        if category_id not in news_by_category or not news_by_category[category_id]:
            print(f"  ⏭️  Skipping empty category: {category_id}")
            continue
            
        md_content = generate_full_markdown_for_category(category_id, category_data, news_by_category[category_id])
        
        # Use mapped filename, default to category_id.md if not found (fallback)
        filename = file_mapping.get(category_id, f"{category_id}.md")
        output_path = os.path.join(sections_dir, filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"  ✅ Saved {filename}")

    print("\\n" + "=" * 60)
    print("✅ All section files generated successfully!")
    
    # Generate Index Readme
    readme_path = os.path.join(os.path.dirname(sections_dir), "readme.md")
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    readme_content = f"""# 📚 Case Study - LLM News Digest

**Latest updates from the LLM ecosystem, curated by category**

*Last Updated: {current_date}*

````{{grid}} 1 2 2 4
:gutter: 3

```{{grid-item-card}}  🛠️ Practical
:link: sections/practical
:link-type: doc
:class-header: sd-bg-success sd-text-white

**Prompt, Agent, MCP**
Hands-on tutorials & implementations
```

```{{grid-item-card}} 💼 Business Cases
:link: sections/business-cases
:link-type: doc
:class-header: sd-bg-warning sd-text-white

**Industry Applications**
ROI studies & Use cases
```

```{{grid-item-card}} 🏢 Big Tech News
:link: sections/bigtech
:link-type: doc
:class-header: sd-bg-primary sd-text-white

**Major Announcements**
OpenAI, Google, Anthropic
```

```{{grid-item-card}} 💡 Insights
:link: sections/insight
:link-type: doc
:class-header: sd-bg-info sd-text-white

**Research & Trends**
Analysis & Thought Leadership
```
````

---

*Generated by [LLM Handbook News Digest](https://github.com/springCoolers/llm-handbook)*
"""

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
        
    print(f"✅ Index README generated at: {readme_path}")
    print("=" * 60)


if __name__ == '__main__':
    main()
