# app/routes/java.py

"""Defines the Java 1.8+ route."""

from flask import Blueprint
from flask_restful import Api
from app.api import create_resource
from app.config import DefaultPorts, OutboundMessages
from app.wrappers import mcstatus_wrapper

java_bp = Blueprint("java", __name__)
api = Api(java_bp)

Full = create_resource(
    "JavaFull",
    mcstatus_wrapper.get_java,
    OutboundMessages.TIMEOUT_JAVA,
    lambda r: r,
    DefaultPorts.JAVA
)

Players = create_resource(
    "JavaPlayerCount",
    mcstatus_wrapper.get_players_java,
    OutboundMessages.TIMEOUT_JAVA,
    lambda r: {"players": r},
    DefaultPorts.JAVA
)

Latency = create_resource(
    "JavaLatency",
    mcstatus_wrapper.get_latency_java,
    OutboundMessages.TIMEOUT_JAVA,
    lambda r: {"latency": r},
    DefaultPorts.JAVA
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
