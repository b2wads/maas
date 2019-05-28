import json

from aioresponses import aioresponses, CallbackResult

from maas.calc.app import app
from tests.base import BaseApiTestCase
from tests.util import plus_service_callback


class CalcEndpointTest(BaseApiTestCase):
    async def setUp(self):
        self.client = await self.aiohttp_client(app)

    async def tearDown(self):
        await super(CalcEndpointTest, self).tearDown()

    async def test_plus_simple_expression(self):
        """
        Confere que conseguimos avaliar uma expressão simples: a + b
        """
        with aioresponses(passthrough=["http://127.0.0.1"]) as rsps:
            rsps.post("http://plus.service", callback=plus_service_callback)
            result = await self.client.post("/eval", json={"expr": "1 + 1"})
            self.assertEqual(result.status, 200)
            data = await result.json()
            self.assertEqual(data, {"result": 2})

    async def test_plus_simple_expression_more_than_one_value(self):
        """
        Confere que conseguimos avaliar uma expressão simples: a + b + c
        """
        with aioresponses(passthrough=["http://127.0.0.1"]) as rsps:
            rsps.post("http://plus.service", callback=plus_service_callback)
            rsps.post("http://plus.service", callback=plus_service_callback)
            result = await self.client.post("/eval", json={"expr": "4 + 1 + 3"})
            self.assertEqual(result.status, 200)
            data = await result.json()
            self.assertEqual(data, {"result": 8})

    async def test_plus_simple_expression_with_negative_numbers(self):
        with aioresponses(passthrough=["http://127.0.0.1"]) as rsps:
            rsps.post("http://plus.service", callback=plus_service_callback)
            rsps.post("http://plus.service", callback=plus_service_callback)
            result = await self.client.post(
                "/eval", json={"expr": "4 + 1 + -3"}
            )
            self.assertEqual(result.status, 200)
            data = await result.json()
            self.assertEqual(data, {"result": 2})

    async def test_plus_simple_expression_with_parenthesis(self):
        with aioresponses(passthrough=["http://127.0.0.1"]) as rsps:
            rsps.post("http://plus.service", callback=plus_service_callback)
            rsps.post("http://plus.service", callback=plus_service_callback)
            result = await self.client.post(
                "/eval", json={"expr": "8 + (1 + -3)"}
            )
            self.assertEqual(result.status, 200)
            data = await result.json()
            self.assertEqual(data, {"result": 6})
