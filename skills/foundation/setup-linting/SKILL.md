---
name: setup-linting
description: Configure ESLint (Flat Config), Prettier, or Biome for strict quality gates. Use for project hardening and enforcing production-grade standards.
metadata:
  security_assessment:
    - "Risk: Low"
    - "Permissions: Local file modification only"

  version: "2.0"
  triggers:
    - "setup linting"
    - "install eslint"
    - "configure prettier"
    - "setup biome"
---

# Linting & Quality Gates

## Core Principles
1. **Strict by Default**: All quality gates (e.g., `no-explicit-any`) set to "error".
2. **Modern Tools**: Use ESLint v9+ (Flat Config) or **Biome** (fast all-in-one alternative).
3. **Automated Enforcement**: Use `husky` and `lint-staged` for pre-commit checks.

## Workflow

### Option A: ESLint + Prettier
- **Install**: `eslint`, `prettier`, `typescript-eslint`, `eslint-config-prettier`.
- **Config**: `eslint.config.mjs` for logic; `.prettierrc` for formatting.
- **Hook**: Add `lint-staged` to run `eslint --fix` and `prettier --write`.

### Option B: Biome (Recommended for Speed)
- **Install**: `@biomejs/biome`.
- **Config**: `biome.json`.
- **Run**: `npx biome check --apply .` for linting, formatting, and imports.

## Best Practices
- **Tailwind Plugin**: If using ESLint/Prettier, include `prettier-plugin-tailwindcss` for class sorting.
- **CI Integration**: Run `lint` and `format:check` in GitHub Actions to block merging of invalid code.
- **Zero Warnings**: Treat warnings as errors in CI (`--max-warnings 0`).

## Pitfalls
- **Legacy Configs**: Delete `.eslintrc` or `.prettierignore` when migrating to Flat Config or Biome.
- **Performance**: Large projects should use Biome or `eslint --cache` to save time.

