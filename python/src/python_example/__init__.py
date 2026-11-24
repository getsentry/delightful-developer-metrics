import logging
import time
import random
import sentry_sdk

from sentry_sdk import metrics
from sentry_sdk.integrations.logging import LoggingIntegration


_PII_DENYLIST_TERMS = ["forwarded", "-ip", "remote-", "via", "-user"]

sentry_sdk.init(
    debug=True,
    attach_stacktrace=False,
    integrations=[LoggingIntegration(level=None, event_level=logging.ERROR)],
    # SDK 3.x collects more by default than 2.x without `send_default_pii`.
    data_collection={
        "user_info": False,
        "http_bodies": [],
        "graphql": {"document": False, "variables": False},
        "gen_ai": {"inputs": False, "outputs": False},
        "mcp": {"inputs": False, "outputs": False},
        "database_query_data": False,
        "queues": False,
        "http_headers": {"request": {"mode": "denylist", "terms": _PII_DENYLIST_TERMS}},
        "cookies": {"mode": "denylist", "terms": _PII_DENYLIST_TERMS},
        "url_query_params": {"mode": "denylist", "terms": _PII_DENYLIST_TERMS},
        "stack_frame_variables": {"mode": "denylist"},
    },
)


def hello():
    start = time.perf_counter()
    time.sleep(0.5 * random.random())
    success = random.random() > 0.5
    metrics.distribution(
        "hello.duration", time.perf_counter() - start, unit="second"
    )
    return success


def main():
    print("Doing things")
    for _ in range(10):
        success = hello()
        metrics.count(
            "hello.said",
            1,
            attributes={
                "success": success,
            },
        )
        print("Did a thing (success = {})".format(success))
    print("Did the things")
