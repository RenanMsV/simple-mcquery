# Simple Minecraft Query Flask RESTful API

A lightweight REST API for querying Minecraft server status (Java, legacy, and Bedrock) using the mcstatus library.  
Perfect for dashboards, bots, and monitoring tools.

## Features
- Supports Java (1.7+), legacy Java (Beta 1.8-1.6), and Bedrock
- Simple REST endpoints
- Lightweight Flask backend
- Ready for [Heroku](https://heroku.com) and [Render](https://render.com) deployment

## Running Locally

### Development server
```
python -m app
```

### Production server (Waitress)
```
waitress-serve --listen=127.0.0.1:3000 wsgi:app
```

[VSCode](https://code.visualstudio.com/) launch configurations are included.

## API Endpoints

Get full server info:
```
GET /api/full/{version}/{ip}/{port}
```

Get player count:
```
GET /api/players/{version}/{ip}/{port}
```

The version parameter in the url can be:
- `java` (1.7+)
- `java_legacy` (Beta 1.8-1.6)
- `bedrock`

### Example
```
https://your-app-url.com/api/full/java/mc.hypixel.net
```

## Deployment

### Heroku
- Uses the included `Procfile` automatically

### Render
- Set start command to:
```
Render.sh
```
