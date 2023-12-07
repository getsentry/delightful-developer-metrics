# Delightful Developer Metrics

Welcome to Sentry's custom metrics alpha.  This repository collects all the relevant information
to get you started quickly including some samples.  We're going to keep this updated as more
features become available.

In order to use this, you need to be rolled into our alpha testing program.

## Sending Metrics

At the moment you have the best experience with the Python SDK.  You need at least version
1.38:

```python
from sentry_sdk import init, metrics

init("YOUR_DSN_HERE", _experiments={
    "enable_metrics": True,
    "metric_code_locations": True,
})

# Increment a metric to see how it works
metrics.incr("drank-drinks", 1, tags={"kind": "coffee"})
```

More docs: [Sending Metrics from Python](https://develop.sentry.dev/delightful-developer-metrics/sending-metrics-sdk/).

## Links

**Documentation:**

* [The UI](https://develop.sentry.dev/delightful-developer-metrics/ui/)
* [General Overview](https://develop.sentry.dev/delightful-developer-metrics/)
* [Sending Metrics from Python](https://develop.sentry.dev/delightful-developer-metrics/sending-metrics-sdk/).
* [General Overview](https://develop.sentry.dev/delightful-developer-metrics/)
* [Nitty gritty internals](https://develop.sentry.dev/sdk/metrics/)

**Engage and Give Feedback:**

* [Discord](https://discord.gg/sentry) (`#custom-metrics`)
* [GitHub Discussion](https://github.com/getsentry/sentry/discussions/58584)

## Samples

* [hello-python](python/src/python_example/__init__.py)