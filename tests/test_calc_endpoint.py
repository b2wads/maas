from aioresponses import aioresponses

from maas.calc.app import app
from tests.base import BaseApiTestCase


class CalcEndpointTest(BaseApiTestCase):
    async def setUp(self):
        self.client = await self.aiohttp_client(app)

    async def test_simple_expression_plus(self):
        """
        Confere que conseguimos avaliar uma expressão simples: a + b
        """
        with aioresponses(passthrough=["http://127.0.0.1"]) as rsps:
            rsps.post("http://plus.service", payload={"result": 2})
            result = await self.client.post("/eval", json={"expr": "1 + 1"})
            self.assertEqual(result.status, 200)
            data = await result.json()
            self.assertEqual(data, {"result": 2})
