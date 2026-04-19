---
name: ci-cd
description: Enterprise-grade CI/CD pipelines for Next.js 15+. Optimized for GitHub Actions, Turborepo, and Vercel. Focuses on build caching, standalone artifacts, and secure environment management.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Medium"
    - "Permissions: GitHub Actions workflow creation"
  triggers:
    - "setup github actions"
    - "configure ci/cd"
    - "next.js deployment pipeline"
    - "turborepo cache ci"
    - "vercel build config"
---

# CI/CD Pipelines (Next.js 15+)

## Core Strategy
1. **Build Once, Deploy Many**: Create a single `standalone` artifact and promote it through environments (Staging -> Production).
2. **Aggressive Caching**: Persist `.next/cache` and `node_modules` to cut build times by up to 80%.
3. **Security First**: Use GitHub Secrets and Environments for sensitive data.

## 1. GitHub Actions Workflow
A standard pipeline should include:
- **Lint & Type Check**: Fail fast if the code doesn't meet quality standards.
- **Unit & E2E Tests**: Ensure the app functions correctly.
- **Build**: Generate the `output: 'standalone'` bundle.
- **Deploy**: Push to Vercel, AWS, or Docker registry.

## 2. Next.js Optimization
In `next.config.js`:
```js
module.exports = {
  output: 'standalone', // Essential for efficient CI artifacts
}
```

## 3. Caching Examples (GitHub Actions)
```yaml
- name: Restore Next.js cache
  uses: actions/cache@v4
  with:
    path: ${{ github.workspace }}/.next/cache
    key: ${{ runner.os }}-nextjs-${{ hashFiles('**/package-lock.json') }}-${{ hashFiles('**.[jt]s', '**.[jt]sx') }}
    restore-keys: |
      ${{ runner.os }}-nextjs-${{ hashFiles('**/package-lock.json') }}-
```

## 4. Turborepo Integration
If using a monorepo, enable Remote Caching:
- Set `TURBO_TOKEN` and `TURBO_TEAM` secrets.
- Use `npx turbo build --cache-dir=".turbo"` for persistent local cache.

## 5. Deployment Patterns
- **Preview Deployments**: Automated for every Pull Request.
- **Production Rollouts**: Protected by manual approval gates in GitHub Environments.
- **Rollbacks**: Tag every successful build to allow instant rollback via Vercel or Git tags.

## Gotchas
- **Fetch Caching (v15)**: Next.js 15 defaults `fetch` to `no-store`. Ensure your CI environment matches the production data fetching strategy.
- **Shallow Clones**: `actions/checkout` defaults to `fetch-depth: 1`. Set to `0` if using Turborepo's `--filter` based on git history.

## Verification Checklist
- [ ] `output: 'standalone'` is enabled in `next.config.js`.
- [ ] GitHub Actions workflow includes caching for `.next/cache`.
- [ ] Secrets are stored in GitHub Secrets, not committed.
- [ ] Pipeline includes a "Lint" and "Test" stage before "Build".
- [ ] Production deployments require a manual approval step.
