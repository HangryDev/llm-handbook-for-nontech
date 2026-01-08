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
            {"name": "Latent Space", "url": "https://latent.space/feed", "count": 3},
            {"name": "Ahead of AI", "url": "https://magazine.sebastianraschka.com/feed", "count": 3},
            {"name": "Anthropic News", "url": "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_news.xml", "count": 3},
            {"name": "Dev.to AI", "url": "https://dev.to/feed/tag/ai", "count": 5},
        ]
    },
    "business": {
        "title": "💼 Business Cases",
        "color": "#e67e22",
        "feeds": [
            {"name": "Harvard Business Review", "url": "http://feeds.hbr.org/harvardbusiness", "count": 3},
            {"name": "The Sequence", "url": "https://thesequence.substack.com/feed", "count": 3},
        ]
    },
    "big_tech": {
        "title": "🏢 Big Tech News",
        "color": "#e74c3c",
        "feeds": [
            {"name": "OpenAI Blog", "url": "https://openai.com/blog/rss.xml", "count": 3},
            {"name": "Google AI Blog", "url": "http://googleaiblog.blogspot.com/atom.xml", "count": 3},
        ]
    },
    "insights": {
        "title": "💡 Insights (General)",
        "color": "#27ae60",
        "feeds": [
            {"name": "MIT Technology Review", "url": "https://www.technologyreview.com/feed/", "count": 3},
            {"name": "Ben's Bites", "url": "https://www.bensbites.com/feed", "count": 3},
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


def generate_markdown(news_by_category):
    """카테고리별 뉴스를 마크다운으로 생성"""

    current_date = datetime.now().strftime("%Y-%m-%d")

    md_content = f"""# 📚 Case Study - LLM News Digest

**Latest updates from the LLM ecosystem, curated by category**

*Last Updated: {current_date}*

---

"""

    # 각 카테고리별로 뉴스 정리
    for category_id, category_data in FEED_CONFIG.items():
        if category_id not in news_by_category or not news_by_category[category_id]:
            continue

        category_title = category_data['title']
        category_color = category_data['color']

        md_content += f"\n## {category_title}\n\n"
        md_content += "```{raw} html\n"
        md_content += f'<div style="font-family: Arial, sans-serif; display: flex; flex-direction: column; gap: 12px; margin-bottom: 20px;">\n\n'

        # 카테고리 내 뉴스 목록
        for source_name, articles in news_by_category[category_id].items():
            for article in articles:
                date_str = article['date'].strftime("%Y.%m.%d")

                # 이미 clean_html로 정리되었으므로 추가 이스케이프 불필요
                # 하지만 안전을 위해 기본적인 HTML 특수문자만 이스케이프
                title = article['title'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                summary = article['summary'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

                md_content += f'''  <!-- {source_name} -->
  <div style="background: white; border-left: 4px solid {category_color}; border-radius: 8px; padding: 15px; box-shadow: 0 2px 6px rgba(0,0,0,0.08);">
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
      <span style="background: {category_color}; color: white; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem;">{source_name}</span>
      <span style="color: #666; font-size: 0.85rem;">📅 {date_str}</span>
    </div>
    <a href="{article['url']}" target="_blank" style="text-decoration: none;">
      <b style="font-size: 1rem; color: #333;">{title}</b>
    </a>
    <p style="color: #666; font-size: 0.9rem; margin-top: 8px; margin-bottom: 0;">{summary}</p>
  </div>

'''

        md_content += "</div>\n```\n\n"

    # Footer
    md_content += """---

## 📖 About This Digest

This digest is automatically generated from curated RSS feeds across four categories:

1. **Practical**: Hands-on tutorials, prompts, agents, and MCP implementations
2. **Business**: Use cases, ROI studies, and industry applications
3. **Big Tech**: Official announcements from OpenAI, Google, Anthropic, etc.
4. **Insights**: Research papers, trend analysis, and thought leadership

### Data Sources

- 🔵 Practical: Latent Space, Ahead of AI, Anthropic News, Dev.to
- 🟠 Business: Harvard Business Review, The Sequence
- 🔴 Big Tech: OpenAI Blog, Google AI Blog
- 🟢 Insights: MIT Technology Review, Ben's Bites

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
        print(f"\n📂 Processing category: {category_data['title']}")

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

    print(f"\n{'=' * 60}")
    print(f"✅ Total: {total_articles} articles collected")
    print(f"{'=' * 60}\n")

    # 마크다운 생성
    print("📝 Generating markdown...")
    md_content = generate_markdown(news_by_category)

    # 파일 저장
    output_path = "/home/robert/work/llm_knowledge_foundation/llm-handbook/_contents/llm-engineering/news/case-study/readme.md"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    print(f"✅ Markdown saved to: {output_path}")
    print("\n" + "=" * 60)
    print("✅ Case Study News Digest generation complete!")
    print("=" * 60)


if __name__ == '__main__':
    main()
