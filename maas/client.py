from aiohttp import ClientSession, ClientTimeout

from maas.conf import settings

default_http_client_timeout = ClientTimeout(total=5, connect=5)


class MathClient:
    def __init__(self):
        self.session = ClientSession(timeout=default_http_client_timeout)

    async def plus(self, left: int, right: int):
        payload = {"left": left, "right": right}
        resp = await self.session.post(
            settings.PLUS_SERVICE_ADDRESS, json=payload
        )
        return await resp.json()
