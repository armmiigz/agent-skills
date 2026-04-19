# Structured Logger Reference

This reference defines the standard for implementing a structured, production-grade logger in Next.js 15+ using **Pino**.

## 1. Core Implementation
Use this pattern to create a centralized logger that ensures consistent formatting and metadata.

```typescript
import pino from 'pino';

export const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  formatters: {
    level: (label) => {
      return { level: label.toUpperCase() };
    },
  },
  timestamp: pino.stdTimeFunctions.isoTime,
});
```

## 2. Request Correlation
To track a single request across multiple logs, use a child logger with a `requestId`.

```typescript
// Create a contextual logger for a specific request
export const createRequestLogger = (requestId: string) => {
  return logger.child({ requestId });
};
```

## 3. Best Practices
- **Never log PII**: Ensure emails, passwords, and tokens are redacted.
- **Use Levels correctly**: 
  - `info`: Key milestones in the application flow.
  - `warn`: Recoverable issues or unexpected states.
  - `error`: Actionable failures (requires intervention).
- **Avoid string interpolation**: Use `logger.info({ userId }, 'message')` instead of `logger.info(\`User ${userId} logged in\`)`.
