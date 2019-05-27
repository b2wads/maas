import os

os.environ["ENV"] = "TEST"

os.environ["TEST_PLUS_SERVICE_ADDRESS"] = os.getenv(
    "TEST_PLUS_SERVICE_ADDRESS", "http://plus.service"
)

assert os.environ["ENV"] == "TEST"
