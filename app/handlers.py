# app/handlers.py

"""The handler responsible for handling queries."""

from datetime import datetime
from http import HTTPStatus
import socket
from app.extensions import logger


def handle_query(func, timeout_msg, extractor=None):
    """Handles the query and returns the result.
    Will return an error if something goes wrong.
    """
    try:
        result = func()

        if extractor:
            result = extractor(result)

        return {
            "cached_at": datetime.now().isoformat(),
            "message": result
        }, HTTPStatus.OK

    except socket.gaierror as e:
        logger.error("DNS resolution failed: %s", e)  # no full traceback
        return {
            "cached_at": datetime.now().isoformat(),
            "error": {
                "type": "dns_error",
                "message": "DNS resolution failed for this address."
            },
        }, HTTPStatus.UNPROCESSABLE_ENTITY

    except (TimeoutError, socket.timeout):
        return {
            "cached_at": datetime.now().isoformat(),
            "error": {
                "type": "network_timeout_error",
                "message": timeout_msg
            }
        }, HTTPStatus.GATEWAY_TIMEOUT

    except ConnectionError:
        logger.exception("Connection error occurred")
        return {
            "cached_at": datetime.now().isoformat(),
            "error": {
                "type": "network_error",
                "message": "A network error occurred."
            },
        }, HTTPStatus.BAD_GATEWAY

    except OSError:
        logger.exception("Unhandled network error")
        return {
            "cached_at": datetime.now().isoformat(),
            "error": {
                "type": "network_error",
                "message": "A network error occurred."
            },
        }, HTTPStatus.BAD_GATEWAY

    except RuntimeError:
        logger.exception("Unhandled error")
        return {
            "cached_at": datetime.now().isoformat(),
            "error": {
                "type": "internal_error",
                "message": "Internal server error."
            },
        }, HTTPStatus.INTERNAL_SERVER_ERROR
