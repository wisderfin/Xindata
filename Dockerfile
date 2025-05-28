FROM python:3.11-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml .
COPY app/ ./app/
COPY .env ./app/.env

RUN uv venv
RUN uv pip install --no-cache-dir .

ENV PATH="/app/.venv/bin:$PATH"
