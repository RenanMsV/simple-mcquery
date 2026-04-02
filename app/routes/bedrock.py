# app/routes/bedrock.py

"""Defines the Bedrock route."""

from flask import Blueprint
from flask_restful import Api
from app.api import create_resource
from app.config import DefaultPorts, OutboundMessages
from app.wrappers import mcstatus_wrapper

bedrock_bp = Blueprint("bedrock", __name__)
api = Api(bedrock_bp)

Full = create_resource(
    "BedrockFull",
    mcstatus_wrapper.get_bedrock,
    OutboundMessages.TIMEOUT_BEDROCK,
    lambda r: r,
    DefaultPorts.BEDROCK
)

Players = create_resource(
    "BedrockPlayerCount",
    mcstatus_wrapper.get_players_bedrock,
    OutboundMessages.TIMEOUT_BEDROCK,
    lambda r: {"players": r},
    DefaultPorts.BEDROCK
)

Latency = create_resource(
    "BedrockLatency",
    mcstatus_wrapper.get_latency_bedrock,
    OutboundMessages.TIMEOUT_BEDROCK,
    lambda r: {"latency": r},
    DefaultPorts.BEDROCK
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

api.add_resource(
    Latency,
    "/latency/<string:ip>",
    "/latency/<string:ip>/<string:port>"
)
