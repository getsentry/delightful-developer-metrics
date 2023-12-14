import './style.css'
import { setupCounter } from './counter.ts'
import * as Sentry from '@sentry/browser';

Sentry.init({
  dsn: import.meta.env.VITE_SENTRY_DSN,
  integrations: [new Sentry.metrics.MetricsAggregator()],
});

document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
  <div>
    <h1>Sentry Metrics</h1>
    <div class="card">
      <button id="counter" type="button">Increment Counter</button>
    </div>
  </div>
`

setupCounter(document.querySelector<HTMLButtonElement>('#counter')!)
