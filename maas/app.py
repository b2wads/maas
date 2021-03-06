from aiohttp import web
from asyncworker import App, RouteTypes

from contrib.parser import Tree

app = App("", "", "", 1)


@app.route(["/"], type=RouteTypes.HTTP, methods=["POST"])
async def operation(request: web.Request):
    return web.json_response({})
