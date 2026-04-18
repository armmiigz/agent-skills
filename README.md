# Agent Skills

A curated collection of skills designed to extend the capabilities of AI coding agents (Claude Code, Cursor, Antigravity, etc.). These skills provide packaged instructions, technical references, and scripts to handle specific, complex workflows.

## Project Structure (Categorized)

Skills are organized into categories for better discoverability and context management:

- **foundation/**: Core project setup and agent management.
  - [skill-creator](./skills/foundation/skill-creator/SKILL.md): Meta-skill for creating and improving other skills.
  - [setup-linting](./skills/foundation/setup-linting/SKILL.md): Modern ESLint (Flat Config), Prettier, and Biome.
  - [architecture](./skills/foundation/architecture/SKILL.md): Standard project structure for Next.js 15+ apps.
  - [architecture-decision-records](./skills/foundation/architecture-decision-records/SKILL.md): Documenting technical decisions (ADRs).
  - [testing](./skills/foundation/testing/SKILL.md): Vitest and Playwright testing strategy.
  - [ci-cd](./skills/foundation/ci-cd/SKILL.md): GitHub Actions pipelines and build optimization.
  - [project-documentation](./skills/foundation/project-documentation/SKILL.md): Automated Changelogs, JSDoc, and API docs.
  - [observability](./skills/foundation/observability/SKILL.md): Structured logging, correlation IDs, and monitoring.
  - [component-engineering](./skills/foundation/component-engineering/SKILL.md): Storybook, scaffolding, and hook patterns.
  - [monorepo-strategy](./skills/foundation/monorepo-strategy/SKILL.md): Scaling with Turborepo and shared packages.
- **frontend/**: UI, CSS, and user experience.
  - [nextjs](./skills/frontend/nextjs/SKILL.md): Next.js 15+ Ultimate Guide (RSC, Actions, PPR).
  - [shadcn-ui](./skills/frontend/shadcn-ui/SKILL.md): shadcn/ui components with Tailwind v4.
  - [ui-foundations](./skills/frontend/ui-foundations/SKILL.md): Design systems with Tailwind v4 and OKLCH.
  - [react-best-practices](./skills/frontend/react-best-practices/SKILL.md): Vercel-grade React performance rules.
  - [composition-patterns](./skills/frontend/composition-patterns/SKILL.md): Flexible component architecture.
  - [view-transitions](./skills/frontend/view-transitions/SKILL.md): Smooth, native-feeling page animations.
  - [state-management](./skills/frontend/state-management/SKILL.md): TanStack Query and Zustand patterns.
  - [i18n](./skills/frontend/i18n/SKILL.md): Multi-language support with next-intl.
  - [accessibility](./skills/frontend/accessibility/SKILL.md): WCAG 2.1 compliance and inclusive design.
  - [advanced-ui](./skills/frontend/advanced-ui/SKILL.md): Complex tables, Framer Motion, and UX flows.
  - [performance-audit](./skills/frontend/performance-audit/SKILL.md): Core Web Vitals and Lighthouse 100/100.
- **backend/**: Server-side logic and APIs.
  - [api-services](./skills/backend/api-services/SKILL.md): Type-safe APIs with better-auth and Zod.
  - [app-security](./skills/backend/security/SKILL.md): Hardening, CSP nonces, and Rate Limiting.
- **database/**: Data persistence and modeling.
  - [drizzle-orm](./skills/database/drizzle-orm/SKILL.md): Drizzle ORM schema and migrations.
- **architecture/**: System design and maintenance.
  - [engineering-standards](./skills/architecture/engineering-standards/SKILL.md): Tech debt, coverage, and quality.
- **testing/**: Advanced testing patterns.
  - [api-mocking](./skills/testing/api-mocking/SKILL.md): Decoupled development with MSW.
- **typescript/**: Language-specific expertise.
  - [typescript-advanced](./skills/typescript/typescript-advanced/SKILL.md): Advanced TypeScript patterns and safety.
- **ai-engineering/**: AI development and testing.
  - [evaluation-harness](./skills/ai-engineering/evaluation-harness/SKILL.md): Systematic LLM evaluation and regression testing.
  - [prompt-engineering](./skills/ai-engineering/prompt-engineering/SKILL.md): Designing and optimizing LLM prompts.
- **domain/finance/**: Financial knowledge and engineering.
  - [wealth-management](./skills/domain/finance/wealth-management/SKILL.md): Personal finance, budgeting, and net worth.
  - [investment-strategy](./skills/domain/finance/investment-strategy/SKILL.md): Asset allocation and portfolio management.
  - [financial-math](./skills/domain/finance/financial-math/SKILL.md): Core formulas (XIRR, CAGR) and precision math.

## How to Create a New Skill

Use the `skill-creator` to scaffold new skills following our standards:

1. Ask your agent: "Create a new skill for [your topic]"
2. The agent will run:
   ```bash
   python scripts/scaffold-skill.py --name "your-skill-name" --category "appropriate-category"
   ```
3. Follow the generated `SKILL.md` template.

## How to Use

### 1. Claude Code

To add a skill to your local Claude Code environment:

```bash
cp -r skills/{category}/{skill-name} ~/.claude/skills/
```

### 2. Claude.ai / Cursor / IDE Agents

Point your agent to the relevant `SKILL.md` file or upload the directory content to your project context.

## Repository Structure

- `skills/`: Categorized root directory for all skills.
- `AGENT.md`: Guidelines for creating and contributing new skills.
