---
name: app-security
description: Defense-in-depth security for Next.js 15+. Covers Server Action hardening, Content Security Policy (CSP) with nonces, Rate Limiting, and sensitive data protection using Taint APIs.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: Local file modification only"
  triggers:
    - "setup security"
    - "hardening server actions"
    - "configure csp"
    - "rate limiting next.js"
    - "prevent xss"
    - "csrf protection"
---

# Application Security (Next.js 15+)

## Core Philosophy
1. **Zero Trust**: Treat Server Actions and Route Handlers as public APIs. Never trust client data.
2. **Defense in Depth**: Use multiple layers (Middleware, WAF, Zod, Auth) to protect resources.
3. **Fail Securely**: Use TypeScript and Zod to ensure inputs are strictly validated before execution.

## 1. Hardening Server Actions
Server Actions are public POST endpoints. They must be secured manually.
- **Authentication**: Check session/token at the start of every action.
- **Authorization**: Verify the user has the right to perform the specific action (Role-Based Access Control).
- **Input Validation**: Use **Zod** for strict schema validation.
```tsx
export async function updateProfile(formData: FormData) {
  const session = await auth();
  if (!session) throw new Error("Unauthorized");
  
  const validated = ProfileSchema.parse(Object.fromEntries(formData));
  // execute logic...
}
```

## 2. Content Security Policy (CSP)
Protect against XSS by restricting where scripts can be loaded from.
- **Strict CSP**: Use nonces generated in `middleware.ts`.
- **Nonces**: A unique token for each request that allows only trusted scripts to run.
- **Headers**: Set `Content-Security-Policy` with `script-src 'nonce-...';`.

## 3. Rate Limiting
Prevent brute-force and scraping.
- **Identifiers**: Use `headers().get('x-forwarded-for')` for IP or `session.user.id` for authenticated users.
- **Tools**: Use `Upstash` or `Redis` for distributed rate limiting.
- **Response**: Return a 429 status or a user-friendly "Too many requests" error.

## 4. Sensitive Data Protection (Taint APIs)
Prevent sensitive server-side objects from leaking to the client.
- **`taintObjectReference`**: Mark an object (e.g., a User object with a password hash) as "do not pass to client".
- **`taintUniqueValue`**: Mark a specific value (e.g., an API key).

## Gotchas
- **HttpOnly Cookies**: Always use `httpOnly: true` and `secure: true` for session cookies. Never store sensitive tokens in `localStorage`.
- **CSRF**: Next.js provides built-in CSRF protection for Server Actions by checking the `Origin` header. Do not disable this.

## Verification Checklist
- [ ] Every Server Action checks for authentication and authorization.
- [ ] All inputs are validated with Zod.
- [ ] CSP with nonces is enabled in `middleware.ts`.
- [ ] Rate limiting is implemented for sensitive endpoints (Login, Signup).
- [ ] Sensitive database objects are tainted or filtered before being passed to components.
