import os

os.environ["ENV"] = "TEST"

os.environ["TEST_PLUS_SERVICE_ADDRESS"] = os.getenv(
    "TEST_PLUS_SERVICE_ADDRESS", "http://plus.service"
)

os.environ["TEST_ASYNCWORKER_HTTP_PORT"] = os.getenv(
    "TEST_ASYNCWORKER_HTTP_PORT", "9999"
)


assert os.environ["ENV"] == "TEST"
