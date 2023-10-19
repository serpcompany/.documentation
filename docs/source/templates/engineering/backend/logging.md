---
title: Logging
sidebar: Handbook
showTitle: true
---

# Logging

As a general rule, we should have logs for every expected and unexpected actions of the application, using the appropriate _log level_.

We should also be logging these exceptions to [Sentry](https://sentry.io/organizations/posthog2/issues/) with the [Sentry Python SDK](https://docs.sentry.io/platforms/python/). Python exceptions should almost always be captured automatically without extra instrumentation, but custom ones (such as failed requests to external services, query errors, or Celery task failures) can be tracked using `capture_exception()`.

### Levels

A _log level_ or _log severity_ is a piece of information telling how important a given log message is:

* `DEBUG`: should be used for information that may be needed for diagnosing issues and troubleshooting or when running application
in the test environment for the purpose of making sure everything is running correctly
* `INFO`: should be used as standard log level, indicating that something happened
* `WARN`: should be used when something unexpected happened but the code can continue the work
* `ERROR`: should be used when the application hits an issue preventing one or more functionalities from properly functioning

## Format

`django-structlog` is the default logging library we use (see [docs](https://django-structlog.readthedocs.io/en/latest/)).
It's a _structured logging_ framework that adds cohesive metadata on each logs that makes it easier to track events or incidents.

Structured logging means that you don’t write hard-to-parse and hard-to-keep-consistent prose in your logs
but that you log events that happen in a context instead.
