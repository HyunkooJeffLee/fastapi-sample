FROM python:3.13-slim AS base

# uv 설치
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \
 && curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:${PATH}"
WORKDIR /app

# 의존성 캐시 레이어
COPY pyproject.toml ./
# uv.lock 있으면 캐시 향상 (없어도 동작)
# COPY uv.lock ./

RUN uv sync --no-dev

# 앱 소스
COPY . .
