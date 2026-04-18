---
name: monorepo-strategy
description: Standardized monorepo architecture for scaling Next.js 15+ projects. Covers Turborepo orchestration, shared packages (UI, Utils, Config), pnpm workspaces, and deployment optimization.
metadata:
  version: "1.0"
  triggers:
    - "setup monorepo"
    - "configure turborepo"
    - "add shared package"
    - "pnpm workspace config"
    - "monorepo deployment"
---

# Monorepo Strategy (Turborepo)

## Core Philosophy
1. **Single Source of Truth**: Shared logic, UI, and config reside in `packages/`, used by multiple `apps/`.
2. **Speed via Caching**: Use Turborepo to cache build and test results locally and in CI.
3. **Decoupled Apps**: Apps in `apps/` should focus only on their specific business domain and deployment.

## 1. Directory Structure (Standard 2025)
```text
├── apps/               # Deployable Applications
│   ├── web/            # Next.js 15 Main App
│   └── admin/          # Admin Dashboard
├── packages/           # Internal Shared Libraries
│   ├── ui/             # Shared shadcn/ui components
│   ├── utils/          # Shared business logic & helpers
│   ├── config-ts/      # Shared TypeScript base configs
│   └── config-eslint/  # Shared Linting/Formatting configs
├── package.json        # Root dependencies
├── pnpm-workspace.yaml # Workspace definitions
└── turbo.json          # Pipeline orchestration
```

## 2. Turborepo Orchestration (`turbo.json`)
Define the pipeline to handle task dependencies:
```json
{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "dist/**"]
    },
    "lint": {
      "outputs": []
    },
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}
```

## 3. Package Management (pnpm)
Use **pnpm workspaces** for speed and efficient disk usage.
- **Root**: `pnpm add -w <pkg>` for tools used everywhere (e.g., `turbo`).
- **Workspace**: `pnpm add <pkg> --filter <app-name>` for specific app dependencies.
- **Local Linking**: Use `"@repo/ui": "workspace:*"` in `package.json` to link internal packages.

## 4. Shared UI Package Pattern
Don't just copy-paste. Build a real internal library.
- Export components from `packages/ui`.
- Consume them in `apps/web` with `import { Button } from "@repo/ui/button"`.
- Ensure `transpilePackages: ["@repo/ui"]` is in `next.config.js`.

## 5. Deployment Optimization
- **`turbo prune`**: Create a minimal subset of the monorepo for Docker builds.
- **Standalone Build**: Use `output: 'standalone'` in Next.js to reduce image size.

## Verification Checklist
- [ ] `turbo.json` has a correctly defined pipeline.
- [ ] `pnpm-workspace.yaml` includes `apps/*` and `packages/*`.
- [ ] Shared packages use the `workspace:*` protocol.
- [ ] Internal packages are correctly transpiled in Next.js apps.
- [ ] Build cache works (running `pnpm build` twice shows `>>> FULL TURBO`).
