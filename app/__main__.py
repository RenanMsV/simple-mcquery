"""A simple Flask Restful API for getting information about Minecraft servers.
Works with Java and Bedrock servers.
"""
from .app import app
from .app import PORT

if __name__ == "__main__":  # this only runs when local testing
    app.run(
        debug=True,  # debug on for local testing
        host='0.0.0.0',
        port=PORT
    )
