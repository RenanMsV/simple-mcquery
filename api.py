import os
from flask import Flask
from flask_restful import Resource, Api
from flask_caching import Cache
import simple_mcquery

app = Flask("Simple MCQuery API")
mcquery_api = Api(app)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})

cache_timeout = 120

class Root(Resource):
  def get(self):
    return {}, 400

class QueryServerJava(Resource):
  @cache.cached(timeout=cache_timeout)
  def get(self, ip, port = "25565"):
    result = simple_mcquery.get_java(ip, port)
    return { "online" : result["player_count"], "more" : result["more"], "cached_for": str(cache_timeout) }, 200

class QueryServerBedrock(Resource):
  @cache.cached(timeout=cache_timeout)
  def get(self, ip, port = "19132"):
    result = simple_mcquery.get_bedrock(ip, port)
    return { "online" : result["player_count"], "more" : result["more"], "cached_for": str(cache_timeout) }, 200

mcquery_api.add_resource(Root, '/')
mcquery_api.add_resource(QueryServerJava, '/api/players/java/<string:ip>', '/api/players/java/<string:ip>/<string:port>')
mcquery_api.add_resource(QueryServerBedrock, '/api/players/bedrock/<string:ip>', '/api/players/bedrock/<string:ip>/<string:port>')

if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 80)))
