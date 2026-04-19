---
name: project-documentation
description: Maintain professional project documentation. Covers automated Changelogs (Keep a Changelog), Type-safe API docs (OpenAPI/Swagger), and standardized JSDoc for TypeScript.
metadata:
  version: "1.0"
  security_assessment:
    - "Risk: Low"
    - "Permissions: Local file modification only"
  triggers:
    - "create changelog"
    - "generate api docs"
    - "document typescript code"
    - "jsdoc standards"
    - "write release notes"
---

# Project Documentation Standard

## 1. Automated Changelogs
Follow the [Keep a Changelog](https://keepachangelog.com/) standard and [Semantic Versioning](https://semver.org/).
- **Types**: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`.
- **Workflow**: 
  1. Use [Conventional Commits](https://www.conventionalcommits.org/).
  2. Use `git log` to extract changes since last tag.
  3. Generate `CHANGELOG.md` using tools like `git-cliff` or `standard-version`.

## 2. Type-Safe API Docs (OpenAPI)
Generate living documentation from your code (e.g., using Drizzle schemas or Zod).
- **Goal**: Always match the implementation with the documentation.
- **Pattern**: Use `zod-to-openapi` to generate Swagger UI from your Zod schemas.

## 3. JSDoc for TypeScript
Enhance code readability and IDE support.
- **Rules**:
  - Document exported functions, components, and complex types.
  - Use `@param`, `@returns`, and `@example` tags.
  - Keep descriptions concise and imperative.

## 4. Documentation Structure
```text
├── docs/                # Extended guides and tutorials
├── CHANGELOG.md         # History of all notable changes
├── README.md            # Entry point for the project
└── openapi.json         # Generated API specification
```

## Gotchas
- **Outdated Docs**: Documentation that doesn't match the code is worse than no documentation. Automate wherever possible.
- **JSDoc Redundancy**: Don't repeat what the TypeScript type already says (e.g., don't document types in `@param` if TS already has them).

## Verification Checklist
- [ ] `CHANGELOG.md` follows the standard format.
- [ ] Exported functions have JSDoc with examples.
- [ ] API documentation is generated from source-of-truth schemas (e.g., Zod).
- [ ] Version numbers follow Semantic Versioning rules.
