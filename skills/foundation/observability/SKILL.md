---
name: observability
description: Implement professional monitoring and logging. Covers structured logging (Pino/Winston), correlation IDs (Request Tracing), and standardized error handling for production.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: File read/write (for logging config)"
  triggers:
    - "setup logging"
    - "structured logs"
    - "request tracing"
    - "correlation id"
    - "production monitoring"
---

# Observability & Structured Logging

## Core Philosophy
1. **Logs as Data**: Logs should be structured (JSON) so they can be queried by ELK, Datadog, or Axiom.
2. **Correlation**: Every log entry in a request lifecycle must share a unique `requestId` (Correlation ID).
3. **No String Interpolation**: Use objects for context to keep messages clean and searchable.

## 1. Structured Log Schema
```json
{
  "timestamp": "2024-04-18T10:00:00Z",
  "level": "error",
  "message": "User login failed",
  "requestId": "uuid-v4-here",
  "userId": "123",
  "error": {
    "message": "Invalid password",
    "stack": "..."
  }
}
```

## 2. Request Correlation (Next.js Middleware)
Generate or propagate `x-request-id` in every request.
- **Middleware**: Inject the ID into headers.
- **AsyncLocalStorage**: Store the ID for the duration of the request to avoid prop-drilling the logger.

## 3. Standardized Error Handling
- **Server**: Catch errors in a global handler and log them with full context (stack, request params).
- **Client**: Use Sentry or similar to capture unhandled exceptions and link them to the server-side `requestId`.

## 4. Best Practices
- **Levels**: Use `debug` for dev, `info` for flow, `warn` for non-critical issues, and `error` for action-required failures.
- **Sensitive Data**: **Never** log PII (emails, passwords, API keys). Sanitize objects before logging.

## Verification Checklist
- [ ] Logger outputs JSON in production.
- [ ] Every request has a unique `x-request-id` header.
- [ ] Logs include correlation IDs automatically.
- [ ] Sensitive data is redacted from logs.
- [ ] Error logs include stack traces and request context.
