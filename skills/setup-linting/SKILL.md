---
name: setup-linting
description: Use this skill to install and configure ESLint (Flat Config) and Prettier with strict quality gates. Trigger this WHENEVER the user mentions code quality, linting setup, formatting enforcement, or project hardening, ensuring production-grade standards from the start.
license: MIT
compatibility: Designed for any Agent Skills-compliant client (e.g. Claude Code)
metadata:
  version: "1.1"
  triggers:
    - "setup linting"
    - "install eslint"
    - "configure prettier"
    - "strict quality gates"
    - "static analysis"
    - "code quality audit"
    - "enforce formatting"
    - "linting setup"
    - "quality control"
    - "linting dependencies"
---

# Setup Linting Skill

This skill provides a complete setup for automated code quality and formatting. It enforces **Strict Quality Gates** (zero-tolerance for `any`, required return types) to ensure production-grade code standards.

## Core Principles
1. **Strict by Default**: All quality gate rules (like `@typescript-eslint/no-explicit-any`) are set to "error", not "warn".
2. **Modern Standards**: Uses **ESLint Flat Config (v9+)** for better performance and modularity.
3. **Separation of Concerns**: ESLint handles logic and bugs; Prettier handles formatting only.
4. **Pre-commit Checks**: Integrates with `husky` and `lint-staged` to prevent non-compliant code from being committed.

## Workflow
Progress:
- [ ] **Infrastructure**: Install core packages (`eslint`, `prettier`, `typescript-eslint`).
- [ ] **Configuration**: Create `eslint.config.js` and `.prettierrc`.
- [ ] **Execution**: Add `lint` and `format` scripts to `package.json`.
- [ ] **Lockdown**: Set up git hooks for automated checks using Husky.

## Gotchas
- **Config Names**: ESLint v9 REQUIRES `eslint.config.js`. Old `.eslintrc` files will be ignored or cause errors.
- **Node Version**: Ensure Node.js 18+ for compatibility with modern linting engines.
- **Parser Conflicts**: If using experimental TS features (like decorators), ensure `parserOptions` covers them or linting will crash.
- **Prettier Plugin Order**: If using Tailwind, the Prettier plugin must be loaded LAST to ensure class sorting works as expected.

## Quick Setup (Automated)
Run the built-in setup script to initialize a strict quality gate:

```bash
bash ./skills/setup-linting/scripts/setup-lint.sh
```

## Reference Documentation
- [Modern ESLint Configuration](./references/eslint-flat-config.md)
- [Prettier Formatting Engine](./references/prettier-config.md)

