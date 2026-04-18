---
name: architecture-decision-records
description: Create and manage Architecture Decision Records (ADRs) to document significant technical choices and their rationale. Use this WHENEVER a major design decision is made, a new framework is adopted, or a fundamental architectural pattern is changed.
metadata:
  version: "1.0"
  triggers:
    - "write adr"
    - "document architectural decision"
    - "technical decision record"
    - "design trade-offs"
    - "adr template"
---

# Architecture Decision Records (ADR)

## Core Principle
"If it isn't documented, it didn't happen." ADRs capture the **Context**, **Decision**, and **Consequences** of technical choices to avoid "re-deciding" the same issues later.

## When to write an ADR
- Choosing a new core library or framework (e.g., Tailwind v4 vs v3).
- Deciding on a directory structure (e.g., Feature-based vs Type-based).
- Selecting a database or ORM (e.g., Drizzle vs Prisma).
- Changing a fundamental security or auth pattern.

## ADR Lifecycle
`Proposed` → `Accepted` → `Deprecated` → `Superseded`

## Templates

### 1. Standard ADR (MADR)
Use for major decisions with multiple stakeholders.
```markdown
# ADR-0001: [Title]

## Status: Accepted | Proposed | Superseded by ADR-XXXX

## Context
What is the problem we are solving? What are the constraints?

## Considered Options
- **Option A**: [Pros/Cons]
- **Option B**: [Pros/Cons]

## Decision
We chose Option [X] because...

## Consequences
- **Positive**: [Better performance, Type safety]
- **Negative**: [Learning curve, Migration effort]
```

### 2. Lightweight ADR
Use for internal team decisions or smaller projects.
```markdown
# ADR-0012: Adopt [Technology]

**Status**: Accepted
**Context**: [Short description of the problem]
**Decision**: [What we are doing]
**Consequences**: [Good/Bad/Mitigations]
```

## Procedures
1. **Scaffold**: Create a new file in `docs/adr/NNNN-title.md`.
2. **Review**: Submit a PR and invite affected team members to review the rationale.
3. **Accept**: Merge the PR and update the ADR index (`docs/adr/README.md`).
4. **Link**: If this decision supersedes a previous one, update the status of the old ADR and link it.

## Gotchas
- **Revisionism**: Never edit an `Accepted` ADR's decision. If the decision changes, write a *new* ADR that supersedes the old one.
- **Y-Statement**: Avoid being vague. Use the format: "In the context of [X], facing [Y], we decided for [Z], to achieve [W], accepting [V]."

## Verification Checklist
- [ ] Context clearly explains the "Why".
- [ ] Trade-offs (Cons) are honestly documented.
- [ ] Status is explicitly stated.
- [ ] Decision is actionable and specific.
- [ ] ADR is indexed in `docs/adr/README.md`.
