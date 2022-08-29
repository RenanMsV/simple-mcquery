from mcstatus import JavaServer
from mcstatus import BedrockServer

def get_java (ip, port):
  server = JavaServer.lookup(f"{ip}:{port}")
  # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
  status = server.status()
  # players, version, description, favicon, latency
  # players: online: int | max: int | sample: player list optional
  # version: name: str | protocol: int
  full = {
    "players" : str(status.players.online),
    "players_max": str(status.players.max),
    "ping": str(round(status.latency)),
    "version": str(status.version.name),
    "version protocol": str(status.version.protocol),
    "description": str(status.description),
    "ip:port": f"{ip}:{port}",
    #"favicon": str(status.favicon),
  }
  return { "full" : full }

def get_bedrock (ip, port):
  server = BedrockServer.lookup(f"{ip}:{port}")
  status = server.status()
  # players_online, latency, motd, map, gamemode, and players_max
  full = {
    "players" : str(status.players_online),
    "players_max": str(status.players_max),
    "ping": str(round(status.latency)),
    "motd": str(status.motd),
    "map": str(status.map),
    "gamemode": str(status.gamemode),
    "ip:port": f"{ip}:{port}",
  }
  return { "full" : full }

def get_players_java (ip, port):
  server = JavaServer.lookup(f"{ip}:{port}")
  status = server.status()
  return { "player_count" : str(status.players.online) }

def get_players_bedrock (ip, port):
  server = BedrockServer.lookup(f"{ip}:{port}")
  status = server.status()
  return {"player_count" : str(status.players_online) }

  

