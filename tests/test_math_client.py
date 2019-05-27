from aioresponses import aioresponses
from asynctest import TestCase
from yarl import URL

from maas.client import MathClient, default_http_client_timeout


class MathClientTest(TestCase):
    async def setUp(self):
        self.client = MathClient()

    async def test_session_has_default_timeout(self):
        client = MathClient()
        self.assertEqual(client.session._timeout, default_http_client_timeout)

    async def test_plus_calls_right_service_address(self):
        """
            Confere que para valores simples o serviço é chamado com o payload correto
        """
        with aioresponses() as rsps:
            rsps.post("http://plus.service", payload={"result": 10})
            result = await self.client.plus(5, 5)
            request_plus = rsps.requests[("POST", URL("http://plus.service"))][
                0
            ]
            self.assertEqual(result, {"result": 10})
            self.assertEqual(
                request_plus.kwargs["json"], {"left": 5, "right": 5}
            )
