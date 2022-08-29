# Simple Minecraft Query Flask RESTful API

![](https://lh3.googleusercontent.com/ZLjX1kYdkywrtdWpOinDk7IV0jgEiQiPC7uvIN32TGnKu2KcOJo1jmOI1fWHciShPKobNQ=s80)

![](https://miro.medium.com/max/240/1*D0rJozJto_S4eO2ab-qWtQ.jpeg)

This project is setup to run at <https://heroku.com>.

This is a python Flask inferface (RESTful API) between the user and the [py-mine/mcstatus](https://github.com/py-mine/mcstatus) python library.

Development/Production servers:
- To test with the development server (flask run) run: `python wsgi.py`
- To test with the production server (waitress) run: `waitress-serve --port=80 wsgi:app`

Notes:
- The version parameter in the url below can be `java` or `bedrock`
- To get the full information for a server access `https://your-app-name.herokuapp.com/api/full/{version}/{ip}/{port}`
- To get only the player count access `https://your-app-name.herokuapp.com/api/players/{version}/{ip}/{port}`
- You can omit the port in the url to use the default 25565 (java) or 19132 (bedrock).
