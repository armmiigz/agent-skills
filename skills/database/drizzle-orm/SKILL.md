---
name: drizzle-orm
description: Database management with Drizzle ORM. Covers schema design, migrations, and relations for Postgres and SQLite.
metadata:
  version: "1.0"
  triggers:
    - "setup database"
    - "drizzle schema"
    - "database migrations"
    - "sql queries drizzle"
---

# Database (Drizzle ORM)

## Core Concepts
Drizzle is a TypeScript ORM that feels like SQL. It uses a code-first approach for schemas.

## Schema Definition (Postgres Example)
```typescript
import { pgTable, serial, text, timestamp } from "drizzle-orm/pg-core";

export const users = pgTable("users", {
  id: serial("id").primaryKey(),
  name: text("name").notNull(),
  email: text("email").notNull().unique(),
  createdAt: timestamp("created_at").defaultNow(),
});
```

## Relations
```typescript
import { relations } from 'drizzle-orm';

export const usersRelations = relations(users, ({ many }) => ({
  posts: many(posts),
}));
```

## Workflow
1.  **Define Schema**: Create `src/db/schema.ts`.
2.  **Generate Migration**: `npx drizzle-kit generate`
3.  **Push/Migrate**: `npx drizzle-kit push` (for dev) or `migrate` (for prod).
4.  **Query**: Use `db.query` for relational data or `db.select()` for SQL-like queries.

## Best Practices
- **Zod Schema Sync**: Use `drizzle-zod` to automatically generate Zod schemas from your DB tables.
- **Indexes**: Explicitly define indexes for fields used in `WHERE` clauses.
- **Connection Pooling**: Use `postgres` or `pg` with a pooler (like Supabase or Neon) for serverless environments.
- **Transactions**: Always use `db.transaction()` for multi-step mutations that must be atomic.

## Pitfalls
- **N+1 Queries**: Use `.with()` or explicit joins to avoid multiple round-trips.
- **BigInt Overflows**: Be careful with `serial` vs `bigint` in JavaScript; use `string` mode for BigInt if necessary.
