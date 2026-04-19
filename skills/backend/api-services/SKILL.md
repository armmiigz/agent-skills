---
name: backend-services
description: Backend patterns for Node.js/Next.js. Covers Route Handlers, authentication with better-auth, and validation with Zod.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Medium"
    - "Permissions: File read/write (for API setup)"
    - "Network: Handles external Auth and API calls"
  triggers:
    - "setup api"
    - "backend logic"
    - "authentication setup"
    - "better-auth"
    - "zod validation"
---

# Backend & API Services

## Core Stack

- **Framework**: Next.js Route Handlers or Elysia/Hono (if standalone).
- **Auth**: `better-auth` for type-safe, multi-strategy authentication.
- **Validation**: `Zod` for schema-based validation of requests and environment variables.

## Patterns

### 1. Type-Safe Validation

```typescript
import { z } from "zod";

const schema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
});

export async function POST(req: Request) {
  const json = await req.json();
  const result = schema.safeParse(json);

  if (!result.success) {
    return Response.json(result.error.flatten(), { status: 400 });
  }
  // logic...
}
```

### 2. Authentication (better-auth)

```typescript
import { betterAuth } from "better-auth";
import { drizzleAdapter } from "better-auth/adapters/drizzle";

export const auth = betterAuth({
  database: drizzleAdapter(db, { provider: "pg" }),
  emailAndPassword: { enabled: true },
});
```

## Best Practices

- **Middleware for Protection**: Use `auth.getSession()` in middleware or layout for route protection.
- **Error Handling**: Use a centralized error handler or consistent response format (e.g., `{ error: string, code: string }`).
- **Streaming Responses**: For AI or long-running tasks, use `ReadableStream`.
- **Environment Variables**: Validate `process.env` with Zod on startup to prevent runtime crashes.

## Pitfalls

- **Exposing Secrets**: Never return sensitive fields (passwords, tokens) in API responses.
- **Missing CORS**: Ensure proper CORS headers if the API is accessed from different origins.
- **Over-fetching**: Return only the necessary fields to save bandwidth.
