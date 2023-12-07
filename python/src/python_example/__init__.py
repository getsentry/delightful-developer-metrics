import time
import random
import sentry_sdk

from sentry_sdk import metrics


sentry_sdk.init(
    debug=True,
    _experiments={
        "enable_metrics": True,
        "metric_code_locations": True,
    },
)


@metrics.timing("hello.duration")
def hello():
    time.sleep(0.5 * random.random())
    return random.random() > 0.5


def main():
    print("Doing things")
    for _ in range(10):
        success = hello()
        metrics.incr(
            "hello.said",
            tags={
                "success": success,
            },
        )
        print("Did a thing (success = {})".format(success))
    print("Did the things")
