# app/routes/legacy.py

"""Defines the Legacy (Beta 1.8 - 1.6) route."""

from flask import Blueprint
from flask_restful import Api
from app.api import create_resource
from app.config import DefaultPorts, OutboundMessages
from app.wrappers import mcstatus_wrapper

legacy_bp = Blueprint("legacy", __name__)
api = Api(legacy_bp)

Full = create_resource(
    "LegacyFull",
    mcstatus_wrapper.get_java_legacy,
    OutboundMessages.TIMEOUT_LEGACY,
    lambda r: r,
    DefaultPorts.LEGACY
)

Players = create_resource(
    "LegacyPlayerCount",
    mcstatus_wrapper.get_players_java_legacy,
    OutboundMessages.TIMEOUT_LEGACY,
    lambda r: {"players": r},
    DefaultPorts.LEGACY
)

api.add_resource(
    Full,
    "/full/<string:ip>",
    "/full/<string:ip>/<string:port>"
)

api.add_resource(
    Players,
    "/playercount/<string:ip>",
    "/playercount/<string:ip>/<string:port>"
)
