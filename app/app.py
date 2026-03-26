"""A simple Flask RESTful API for getting information about Minecraft servers.
Works with Java and Bedrock servers.
"""
import os
from datetime import datetime
from http import HTTPStatus
from flask import Flask
from flask_restful import Resource, Api
from flask_caching import Cache

from app import __version__
from . import mcstatus_wrapper

PORT = int(os.environ.get("PORT", 80))  # 80 as default, or the configured port
CACHE_TIMEOUT = 120  # The time it takes for the cached result to expire

MSG_TOUT_ERR_JAVA = "TimeoutError. Wrong port, offline or not Java 1.7+"
MSG_TOUT_ERR_JAVA_LEG = "TimeoutError. Wrong port, offline " \
    "or not Java Legacy (Beta 1.8-1.6)"
MSG_TOUT_ERR_BEDROCK = "TimeoutError. Wrong port, offline or not Bedrock"

app = Flask("Simple Minecraft Query RESTful API")
app.url_map.strict_slashes = False
mcquery_api = Api(app)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})


class Root(Resource):
    """Main page route"""
    @cache.cached(timeout=CACHE_TIMEOUT)
    def get(self):
        """Shows info about the API itself."""
        return {
            "status": "online",
            "service": app.name,
            "version": __version__,
            "description": "Query Minecraft Java and Bedrock servers for"
            " player and status information.",
            "routes": {
                "java_get_full_info":
                    "/api/full/java/{ip}/{port?}",
                "java_get_player_count":
                    "/api/playercount/java/{ip}/{port?}",
                "java_legacy_get_full_info":
                    "/api/full/java_legacy/{ip}/{port?}",
                "java_legacy_get_player_count":
                    "/api/playercount/java_legacy/{ip}/{port?}",
                "bedrock_get_full_info":
                    "/api/full/bedrock/{ip}/{port?}",
                "bedrock_get_player_count":
                    "/api/playercount/bedrock/{ip}/{port?}"
            },
            "default_ports": {
                "java": 25565,
                "bedrock": 19132
            },
            "cache": {
                "cache_timeout_ms": CACHE_TIMEOUT * 1000
            }
        }, HTTPStatus.OK


class QueryServerJava(Resource):
    """Route for the Java server query"""
    @cache.cached(timeout=CACHE_TIMEOUT)
    def get(self, ip, port="25565"):
        """Get HTTP method"""
        try:
            result = mcstatus_wrapper.get_java(ip, port)
            return {
                "cached_at": datetime.now().isoformat(),
                "message": result["full"],
            }, HTTPStatus.OK
        except TimeoutError:
            return {"message": MSG_TOUT_ERR_JAVA}, HTTPStatus.GATEWAY_TIMEOUT
        except Exception as e:
            print("Error:", str(e))
            return {
                "message": f"{type(e).__name__}. Internal server error."
            }, HTTPStatus.INTERNAL_SERVER_ERROR


class QueryPlayerCountJava(Resource):
    """Route for the Java server players count query"""
    @cache.cached(timeout=CACHE_TIMEOUT)
    def get(self, ip, port="25565"):
        """Get HTTP method"""
        try:
            result = mcstatus_wrapper.get_players_java(ip, port)
            return {
                "cached_at": datetime.now().isoformat(),
                "message": {
                    "player_count": result["player_count"]
                }
            }, HTTPStatus.OK
        except TimeoutError:
            return {"message": MSG_TOUT_ERR_JAVA}, HTTPStatus.GATEWAY_TIMEOUT
        except Exception as e:
            print("Error:", str(e))
            return {
                "message": f"{type(e).__name__}. Internal server error."
            }, HTTPStatus.INTERNAL_SERVER_ERROR


class QueryServerJavaLegacy(Resource):
    """Route for the legacy Java server query"""
    @cache.cached(timeout=CACHE_TIMEOUT)
    def get(self, ip, port="25565"):
        """Get HTTP method"""
        try:
            result = mcstatus_wrapper.get_java_legacy(ip, port)
            return {
                "cached_at": datetime.now().isoformat(),
                "message": result["full"]
            }, HTTPStatus.OK
        except TimeoutError:
            return {
                "message": MSG_TOUT_ERR_JAVA_LEG
            }, HTTPStatus.GATEWAY_TIMEOUT
        except Exception as e:
            print("Error:", str(e))
            return {
                "message": f"{type(e).__name__}. Internal server error."
            }, HTTPStatus.INTERNAL_SERVER_ERROR


class QueryPlayerCountJavaLegacy(Resource):
    """Route for the legacy Java server players count query"""
    @cache.cached(timeout=CACHE_TIMEOUT)
    def get(self, ip, port="25565"):
        """Get HTTP method"""
        try:
            result = mcstatus_wrapper.get_players_java_legacy(ip, port)
            return {
                "cached_at": datetime.now().isoformat(),
                "message": {
                    "player_count": result["player_count"]
                }
            }, HTTPStatus.OK
        except TimeoutError:
            return {
                "message": MSG_TOUT_ERR_JAVA_LEG
            }, HTTPStatus.GATEWAY_TIMEOUT
        except Exception as e:
            print("Error:", str(e))
            return {
                "message": f"{type(e).__name__}. Internal server error."
            }, HTTPStatus.INTERNAL_SERVER_ERROR


class QueryServerBedrock(Resource):
    """Route for the Bedrock server query"""
    @cache.cached(timeout=CACHE_TIMEOUT)
    def get(self, ip, port="19132"):
        """Get HTTP method"""
        try:
            result = mcstatus_wrapper.get_bedrock(ip, port)
            return {
                "cached_at": datetime.now().isoformat(),
                "message": result["full"]
            }, HTTPStatus.OK
        except TimeoutError:
            return {
                "message": MSG_TOUT_ERR_BEDROCK
            }, HTTPStatus.GATEWAY_TIMEOUT
        except Exception as e:
            print("Error:", str(e))
            return {
                "message": f"{type(e).__name__}. Internal server error."
            }, HTTPStatus.INTERNAL_SERVER_ERROR


class QueryPlayerCountBedrock(Resource):
    """Route for the Bedrock server players count query"""
    @cache.cached(timeout=CACHE_TIMEOUT)
    def get(self, ip, port="19132"):
        """Get HTTP method"""
        try:
            result = mcstatus_wrapper.get_players_bedrock(ip, port)
            return {
                "cached_at": datetime.now().isoformat(),
                "message": {
                    "player_count": result["player_count"]
                }
            }, HTTPStatus.OK
        except TimeoutError:
            return {
                "message": MSG_TOUT_ERR_BEDROCK
            }, HTTPStatus.GATEWAY_TIMEOUT
        except Exception as e:
            print("Error:", str(e))
            return {
                "message": f"{type(e).__name__}. Internal server error."
            }, HTTPStatus.INTERNAL_SERVER_ERROR


mcquery_api.add_resource(Root, '/')
mcquery_api.add_resource(
    QueryServerJava,
    '/api/full/java/<string:ip>',
    '/api/full/java/<string:ip>/<string:port>'
)
mcquery_api.add_resource(
    QueryPlayerCountJava,
    '/api/playercount/java/<string:ip>',
    '/api/playercount/java/<string:ip>/<string:port>'
)
mcquery_api.add_resource(
    QueryServerJavaLegacy,
    '/api/full/java_legacy/<string:ip>',
    '/api/full/java_legacy/<string:ip>/<string:port>'
)
mcquery_api.add_resource(
    QueryPlayerCountJavaLegacy,
    '/api/playercount/java_legacy/<string:ip>',
    '/api/playercount/java_legacy/<string:ip>/<string:port>'
)
mcquery_api.add_resource(
    QueryServerBedrock,
    '/api/full/bedrock/<string:ip>',
    '/api/full/bedrock/<string:ip>/<string:port>'
)
mcquery_api.add_resource(
    QueryPlayerCountBedrock,
    '/api/playercount/bedrock/<string:ip>',
    '/api/playercount/bedrock/<string:ip>/<string:port>'
)
