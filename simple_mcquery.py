from mcstatus import JavaServer
from mcstatus import BedrockServer

def get_java (ip, port):
  server = JavaServer.lookup(f"{ip}:{port}")

  # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
  status = server.status()
  # players, version, description, favicon, latency
  # players: online: int | max: int | sample: player list optional
  # version: name: str | protocol: int

  more = {
    "ping": str(round(status.latency)),
    "version": str(status.version.name),
    "version protocol": str(status.version.protocol),
    "description": str(status.description),
    "players_max": str(status.players.max),
    "ip": f"{ip}:{port}",
    #"favicon": str(status.favicon),
  }

  return {"player_count" : str(status.players.online), "more" : more }

def get_bedrock (ip, port):
  print(ip, port)
  server = BedrockServer.lookup(f"{ip}:{port}")
  status = server.status()
  # players_online, latency, motd, map, gamemode, and players_max

  more = {
    "ping": str(round(status.latency)),
    "motd": str(status.motd),
    "map": str(status.map),
    "gamemode": str(status.gamemode),
    "players_max": str(status.players_max),
    "ip": f"{ip}:{port}",
  }
  return {"player_count" : str(status.players_online), "more" : more }
