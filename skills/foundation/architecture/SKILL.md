---
name: architecture
description: Full-stack architecture patterns for Next.js 15+. Defines directory structure, layering, and naming conventions for scalable applications.
metadata:
  version: "1.0"
  triggers:
    - "project structure"
    - "where to put files"
    - "clean architecture"
    - "modular design"
---

# Architecture Skill

## Directory Structure (Next.js 15+)

```text
src/
├── app/              # Routes, Pages, Layouts (Server Components)
├── components/       # Shared UI components
│   ├── ui/           # shadcn/ui components (low-level)
│   └── blocks/       # Complex, feature-agnostic blocks
├── features/         # Domain-specific logic (Modular approach)
│   └── user-profile/
│       ├── components/
│       ├── actions.ts
│       ├── hooks.ts
│       └── schema.ts
├── lib/              # Shared utilities & configs (drizzle, auth, etc.)
├── hooks/            # Global React hooks
├── services/         # Business logic & external API calls
└── types/            # Global TS definitions
```

## Layering Principles

1.  **UI Layer**: React components (Server/Client). Keep them focused on presentation.
2.  **Action Layer**: Next.js Server Actions for mutations. Handles validation and calling services.
3.  **Service Layer**: Pure business logic. Independent of HTTP/Next.js context.
4.  **Data Layer**: Drizzle ORM schemas and database access.

## Naming Conventions
- **Components**: PascalCase (e.g., `UserCard.tsx`).
- **Hooks**: camelCase starting with `use` (e.g., `useAuth.ts`).
- **Actions/Services**: camelCase (e.g., `updateUser.ts`).
- **Files**: kebab-case for everything else.

## Best Practices
- **Feature Encapsulation**: Group related logic in `features/` rather than spreading across global folders.
- **Dependency Direction**: UI depends on Services/Schemas, not the other way around.
- **Zod Everywhere**: Use Zod for runtime validation at the boundary (API, Actions, Forms).
