# app/extensions.py

"""Sets up necessary extensions for the app to work."""

import logging
from flask_caching import Cache
from app.config import APP_ID

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
)
logger = logging.getLogger(APP_ID)

cache = Cache()
