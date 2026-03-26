"""Simple wrapper for the mcstatus package.
"""

from mcstatus import JavaServer
from mcstatus import LegacyServer
from mcstatus import BedrockServer


def get_java(ip, port):
    """Gets a Java server info. Must be Java 1.7+.

    Args:
        ip (str): The server ip
        port (int): The server port

    Returns:
        dict: All the info it found
    """
    server = JavaServer.lookup(f"{ip}:{port}")
    status = server.status()
    full = {
        "players": str(status.players.online),
        "players_max": str(status.players.max),
        "ping": str(round(status.latency)),
        "version": str(status.version.name),
        "version protocol": str(status.version.protocol),
        "description": str(status.description),
        "ip:port": f"{ip}:{port}",
        "icon": str(status.icon)
    }
    return {"full": full}


def get_java_legacy(ip, port):
    """Gets a Java legacy server info. Must be Java (Beta 1.8-1.6).

    Args:
        ip (str): The server ip
        port (int): The server port

    Returns:
        dict: All the info it found
    """
    server = LegacyServer.lookup(f"{ip}:{port}")
    status = server.status()
    full = {
        "players": str(status.players.online),
        "players_max": str(status.players.max),
        "ping": str(round(status.latency)),
        "version": str(status.version.name),
        "version protocol": str(status.version.protocol),
        "description": str(status.description),
        "ip:port": f"{ip}:{port}"
    }
    return {"full": full}


def get_bedrock(ip, port):
    """Gets a Bedrock server info.

    Args:
        ip (str): The server ip
        port (int): The server port

    Returns:
        dict: All the info it found
    """
    server = BedrockServer.lookup(f"{ip}:{port}")
    status = server.status()
    full = {
        "players": str(status.players.online),
        "players_max": str(status.players.max),
        "ping": str(round(status.latency)),
        "motd": str(status.motd),
        "map": str(status.map_name),
        "gamemode": str(status.gamemode),
        "ip:port": f"{ip}:{port}",
    }
    return {"full": full}


def get_players_java(ip, port):
    """Gets the amount of players in a Java server.
    Must be Java (Beta 1.8-1.6).

    Args:
        ip (str): The server ip
        port (int): The server port

    Returns:
        dict[str, int]: A dictionary with the key 'player_count'.
    """
    server = JavaServer.lookup(f"{ip}:{port}")
    status = server.status()
    return {"player_count": str(status.players.online)}


def get_players_java_legacy(ip, port):
    """Gets the amount of players in a Java server. Must be Java 1.7+.

    Args:
        ip (str): The server ip
        port (int): The server port

    Returns:
        dict[str, int]: A dictionary with the key 'player_count'.
    """
    server = LegacyServer.lookup(f"{ip}:{port}")
    status = server.status()
    return {"player_count": str(status.players.online)}


def get_players_bedrock(ip, port):
    """Gets the amount of players in a Bedrock server.

    Args:
        ip (str): The server ip
        port (int): The server port

    Returns:
        dict[str, int]: A dictionary with the key 'player_count'.
    """
    server = BedrockServer.lookup(f"{ip}:{port}")
    status = server.status()
    return {"player_count": str(status.players.online)}


if __name__ == '__main__':
    pass
