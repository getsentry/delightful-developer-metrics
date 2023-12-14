# Browser JavaScript Sentry Metrics Example

A simple example for how to send metrics with Browser JavaScript:

```bash
export VITE_SENTRY_DSN="<your dsn>"
yarn dev
```

Support released with https://github.com/getsentry/sentry-javascript/releases/tag/7.88.0

To enable capturing metrics in your own app, you first need to add the `MetricsAggregator` integration.

```js
Sentry.init({
  dsn: "__DSN__",
  integrations: [new Sentry.metrics.MetricsAggregator()],
});
```

Then you'll be able to add `counters`, `sets`, `distributions`, and `gauges` under the `Sentry.metrics` namespace.

```js
// Add 4 to a counter named `hits`
Sentry.metrics.increment("hits", 4);

// Add 2 to gauge named `parallel_requests`, tagged with `happy: "no"`
Sentry.metrics.gauge("parallel_requests", 2, { tags: { happy: "no" } });

// Add 4.6 to a distribution named `response_time` with unit seconds
Sentry.metrics.distribution("response_time", 4.6, { unit: "seconds" });

// Add 2 to a set named `valuable.ids`
Sentry.metrics.set("valuable.ids", 2);
```
