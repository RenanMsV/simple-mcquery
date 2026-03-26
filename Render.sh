#!/usr/bin/env bash

# WSGI command for Render.com

PORT=${PORT:-5000}
WEB_CONCURRENCY=${WEB_CONCURRENCY:-4}

waitress-serve \
  --listen 0.0.0.0:$PORT \
  --trusted-proxy '*' \
  --trusted-proxy-headers "x-forwarded-for x-forwarded-proto x-forwarded-port" \
  --clear-untrusted-proxy-headers \
  --threads $WEB_CONCURRENCY \
  wsgi:app
