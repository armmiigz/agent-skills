---
name: skill-creator
description: Use this skill to create, modify, and improve other agent skills. Trigger this WHENEVER the user wants to start a new skill project, optimize a skill's description for better triggering, or standardize an existing skill to follow best practices.
license: MIT
compatibility: Designed for any Agent Skills-compliant client (e.g. Claude Code)
metadata:
  version: "1.1"
  triggers:
    - "create new skill"
    - "improve skill"
    - "standardize skill"
    - "benchmarking"
    - "create a new skill"
    - "write a new skill"
    - "new skill creation"
---

# Skill Creator

A meta-skill for designing, implementing, and iteratively improving other skills. It ensures that every skill added to this project adheres to the **Anatomy of a Skill** and **Progressive Disclosure** principles.

## Workflow
Progress:
- [ ] **Discovery**: Define the skill's purpose, triggers, and expected output.
- [ ] **Infrastructure**: Create the folder structure (SKILL.md, references/, scripts/).
- [ ] **Evaluation**: Create test cases in `evals/evals.json` and run benchmarks.
- [ ] **Optimization**: Refine description for ROI and effectiveness.

## Core Standards
- **Anatomy**: Folder structure must include `SKILL.md` and `references/`.
- **Progressive Disclosure**: Keep `SKILL.md` lean; defer details to Level 3 references.
- **Trigger Logic**: Descriptions must be specific and "pushy" to ensure accurate activation.

## Gotchas
- **Over-Instruction**: Too many rules can confuse the agent. Aim for moderate detail; defer to scripts for complex logic.
- **Vague Triggers**: If a skill triggers too often (false positive), narrow the description. If it never triggers, make the description more "pushy" and use imperative language.
- **Overfitting Description**: Avoid adding exact keywords from a single failed prompt. Instead, find the general concept the prompt belongs to.
- **Token Bloat**: Keep `SKILL.md` under 100 lines if possible. Use `references/` for the heavy lifting.

## Technical Resources
Use these reference files for detailed standards and templates:
- [Skill Development Standards](./references/standards.md)
- [Project Schemas & Evaluation](./references/schemas.md)

## Evaluation Scripts
For benchmarking and qualitative review, use the provided scripts:
- `aggregate_benchmark.py`: Compile pass rates, latency, and token data.
- `generate_review.py`: Generate an HTML report for review.

