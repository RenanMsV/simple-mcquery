# app/wrappers/mcstatus_wrapper.py

"""Simple wrapper for the mcstatus package."""

from mcstatus import JavaServer
from mcstatus import LegacyServer
from mcstatus import BedrockServer


def _lookup(server_cls, ip: str, port: int):
    """Helper to lookup and fetch status."""
    server = server_cls.lookup(f"{ip}:{port}")
    return server.status()


def _base_response(ip: str, port: int) -> dict:
    """Base response shared across all server types."""
    return {"ip:port": f"{ip}:{port}"}


def _format_common(status) -> dict:
    """Fields common to most server types."""
    return {
        "players": str(status.players.online),
        "players_max": str(status.players.max),
        "ping": str(round(status.latency)),
    }


def get_java(ip: str, port: int) -> dict:
    """Gets a Java server info. Must be Java 1.7+."""
    status = _lookup(JavaServer, ip, port)

    full = {
        **_base_response(ip, port),
        **_format_common(status),
        "version": str(status.version.name),
        "version_protocol": str(status.version.protocol),
        "description": str(status.description),
        "icon": str(status.icon),
    }

    return full


def get_java_legacy(ip: str, port: int) -> dict:
    """Gets a Java legacy server info (Beta 1.8–1.6)."""
    status = _lookup(LegacyServer, ip, port)

    full = {
        **_base_response(ip, port),
        **_format_common(status),
        "version": str(status.version.name),
        "version_protocol": str(status.version.protocol),
        "description": str(status.description),
    }

    return full


def get_bedrock(ip: str, port: int) -> dict:
    """Gets a Bedrock server info."""
    status = _lookup(BedrockServer, ip, port)

    full = {
        **_base_response(ip, port),
        **_format_common(status),
        "motd": str(status.motd),
        "map": str(status.map_name),
        "gamemode": str(status.gamemode),
    }

    return full


def _get_player_count(server_cls, ip: str, port: int) -> str:
    """Generic player count fetcher."""
    status = _lookup(server_cls, ip, port)
    return str(status.players.online)


def get_players_java(ip: str, port: int) -> str:
    """Gets player count for Java server."""
    return _get_player_count(JavaServer, ip, port)


def get_players_java_legacy(ip: str, port: int) -> str:
    """Gets player count for legacy Java server."""
    return _get_player_count(LegacyServer, ip, port)


def get_players_bedrock(ip: str, port: int) -> str:
    """Gets player count for Bedrock server."""
    return _get_player_count(BedrockServer, ip, port)
