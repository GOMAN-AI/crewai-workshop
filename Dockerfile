FROM python:3.12.12-slim

WORKDIR /app

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  curl docker.io \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && mkdir -p /app/src

COPY pyproject.toml .
COPY entrypoint.sh .

RUN pip install --no-cache-dir -e .

ENTRYPOINT ["/app/entrypoint.sh"]
