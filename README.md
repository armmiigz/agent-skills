# Agent Skills

A curated collection of skills designed to extend the capabilities of AI coding agents (Claude Code, Cursor, Antigravity, etc.). These skills provide packaged instructions, technical references, and scripts to handle specific, complex workflows.

## Available Skills

- **[shadcn/ui](./skills/shadcn-ui/SKILL.md)**: A comprehensive guide for installing, configuring, and using shadcn/ui components in Next.js projects.
- **[ui-foundations](./skills/ui-foundations/SKILL.md)**: A design system skill for creating brand identities using Tailwind v4, OKLCH color palettes, and typographic scales.
- **[skill-creator](./skills/skill-creator/SKILL.md)**: A meta-skill for creating and improving other skills with built-in benchmarking and evaluation scripts.
- **[typescript-advance](./skills/typescript-advance/SKILL.md)**: Expert-level TypeScript patterns for generics, discriminated unions, and strict type safety.
- **[setup-linting](./skills/setup-linting/SKILL.md)**: Modern ESLint (Flat Config) and Prettier setup with strict quality gate enforcement.

## How to Use

### 1. Claude Code
To add a skill to your local Claude Code environment, copy the skill directory to your skills folder:

```bash
cp -r skills/{skill-name} ~/.claude/skills/
```

### 2. Claude.ai (Project Knowledge)
For web-based interactions, you can add any skill to a Claude Project:
1. Open your project on Claude.ai.
2. Click on **Add Content** -> **Upload Files**.
3. Upload the `SKILL.md` and any files in its `references/` or `scripts/` directories.
4. Claude will now have access to these instructions for all messages in the project.

### 3. Cursor / Antigravity / Other IDE Agents
Simply point your agent to the `SKILL.md` file or include it in your project's context/rules.

## Repository Structure
- `skills/`: The root directory for all available skills.
- `AGENT.md`: Comprehensive guidelines for creating and contributing new skills.
