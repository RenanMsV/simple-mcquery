from flask import Flask
from flask_restful import Resource, Api
from flask_caching import Cache
from . import simple_mcquery

app = Flask("Simple MCQuery API")
mcquery_api = Api(app)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})

cache_timeout = 120 # The time it takes for the cached result of the query to expire in seconds

class Root(Resource):
  def get(self):
    return {}, 400

class QueryServerJava(Resource):
  @cache.cached(timeout = cache_timeout)
  def get(self, ip, port = "25565"):
    try:
      result = simple_mcquery.get_java(ip, port)
      return { "full" : result["full"] }, 200
    except TimeoutError:
      return { "message" : "TimeoutError. Server must be offline or not a java server" }
    except Exception as e:
      print("Error:", str(e))
      return { "message" : f"{type(e).__name__}. Internal server error." }

class QueryServerBedrock(Resource):
  @cache.cached(timeout = cache_timeout)
  def get(self, ip, port = "19132"):
    try:
      result = simple_mcquery.get_bedrock(ip, port)
      return { "full" : result["full"] }, 200
    except TimeoutError:
      return { "message" : "TimeoutError. Server must be offline or not a bedrock server" }
    except Exception as e:
      print("Error:", str(e))
      return { "message" : f"{type(e).__name__}. Internal server error." }

class QueryPlayersJava(Resource):
  @cache.cached(timeout = cache_timeout)
  def get(self, ip, port = "25565"):
    try:
      result = simple_mcquery.get_players_java(ip, port)
      return { "players" : result["player_count"] }, 200
    except TimeoutError:
      return { "message" : "TimeoutError. Server must be offline or not a java server" }
    except Exception as e:
      print("Error:", str(e))
      return { "message" : f"{type(e).__name__}. Internal server error." }

class QueryPlayersBedrock(Resource):
  @cache.cached(timeout = cache_timeout)
  def get(self, ip, port = "19132"):
    try:
      result = simple_mcquery.get_players_bedrock(ip, port)
      return { "players" : result["player_count"] }, 200
    except TimeoutError:
      return { "message" : "TimeoutError. Server must be offline or not a bedrock server" }
    except Exception as e:
      print("Error:", str(e))
      return { "message" : f"{type(e).__name__}. Internal server error." }

mcquery_api.add_resource(Root, '/')
mcquery_api.add_resource(QueryServerJava, '/api/full/java/<string:ip>', '/api/full/java/<string:ip>/<string:port>')
mcquery_api.add_resource(QueryServerBedrock, '/api/full/bedrock/<string:ip>', '/api/full/bedrock/<string:ip>/<string:port>')
mcquery_api.add_resource(QueryPlayersJava, '/api/players/java/<string:ip>', '/api/players/java/<string:ip>/<string:port>')
mcquery_api.add_resource(QueryPlayersBedrock, '/api/players/bedrock/<string:ip>', '/api/players/bedrock/<string:ip>/<string:port>')

#if __name__ == '__main__':
#  app.run(debug = False, host = '0.0.0.0', port = int(os.environ.get("PORT", 80)))
