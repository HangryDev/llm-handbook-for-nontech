# syntax=docker/dockerfile:1
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# (선택) lxml 같은 패키지 빌드에서 컴파일이 필요한 경우를 대비
# slim에서 종종 필요합니다. 불필요하면 지워도 됩니다.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libxml2-dev \
    libxslt1-dev \
 && rm -rf /var/lib/apt/lists/*

# 먼저 requirements만 복사해서 캐시를 최대한 활용
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip setuptools wheel \
 && pip install -r /app/requirements.txt \
 && pip install lxml_html_clean

# 프로젝트 파일 복사(필요한 것만)
COPY . /app

# 기본 커맨드(원하시는 빌드/서브커맨드로 바꾸세요)
# 예: jupyter-book build .
CMD ["jupyter-book", "build", "."]


