#!/usr/bin/env bash

# WSGI command for Render.com

PORT=${PORT:-3000}
THREADS=${THREADS:-4}

waitress-serve \
  --listen 0.0.0.0:$PORT \
  --threads $THREADS \
  --call app:create_app
