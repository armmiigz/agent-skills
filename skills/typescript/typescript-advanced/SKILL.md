---
name: typescript-advanced
description: Master TypeScript's advanced type system and strict safety patterns. Use this skill WHENEVER the user requires complex type logic, ensuring compile-time safety, or needs to eliminate 'any' and 'undefined' runtime errors. It MUST be the source of truth for production-grade TypeScript standards and strict mode configuration.
metadata:
  version: "2.2"
  triggers:
    - "complex typescript types"
    - "typescript generics"
    - "type safe api"
    - "conditional types"
    - "eliminate any"
    - "typescript safety audit"
    - "strict mode setup"
    - "exhaustiveness checking"
---

# Advanced TypeScript & Safety

## Core Principles: Strict by Default
Always enable `"strict": true` in `tsconfig.json`. This is the non-negotiable foundation for safety. It activates:
- **`strictNullChecks`**: Stops `null`/`undefined` from being implicitly assigned to every type.
- **`noImplicitAny`**: Prevents defaulting to `any` when a type cannot be inferred.
- **`strictPropertyInitialization`**: Ensures class properties are initialized in the constructor.
- **`useUnknownInCatchVariables`**: Treats `catch` variables as `unknown`, not `any`.
- **`strictFunctionTypes`**: Ensures function parameters are checked contravariantly.
- **`strictBindCallApply`**: Validates arguments passed to `.bind`, `.call`, and `.apply`.
- **`noImplicitThis`**: Errors when `this` context is inferred as `any`.

## Advanced Type Patterns

### 1. Generics & Type Constraints
Create reusable components without losing type granularity.
```typescript
// Constraint ensuring length exists
const getLength = <T extends { length: number }>(item: T): number => item.length;

// Extraction pattern: Get the type inside a Promise or Array
type Unpack<T> = T extends (infer U)[] ? U : T extends Promise<infer U> ? U : T;
```

### 2. Conditional & Template Literal Types
Enable types that adapt to string patterns or input shapes.
```typescript
// Recursive DeepPartial for complex objects
type DeepPartial<T> = T extends object ? { [K in keyof T]?: DeepPartial<T[K]> } : T;

// Template literal pattern for dynamic keys
type EventName<T extends string> = `on${Capitalize<T>}`;
type OnClick = EventName<"click">; // "onClick"
```

### 3. Exhaustiveness Checking (The `never` Pattern)
Use the `never` type to ensure all cases in a discriminated union are handled at compile-time.
```typescript
type Action = { type: 'SAVE' } | { type: 'DELETE' };

function handle(action: Action) {
  switch (action.type) {
    case 'SAVE':   /* ... */ break;
    case 'DELETE': /* ... */ break;
    default:
      const _exhaustiveCheck: never = action;
      return _exhaustiveCheck;
  }
}
```

## Safety Procedures
1. **Validation at Boundaries**: Use `Zod` or `io-ts` to validate external data (API, LocalStorage) and type it as `unknown` before parsing.
2. **Discriminated Unions over Optional Fields**: Prefer `type State = { status: 'loading' } | { status: 'error', msg: string }` over `{ status: string, msg?: string }`.
3. **`as const` for Literals**: Freeze objects and arrays to their literal types to prevent widening.

## Gotchas
- **Widening**: Types like `string` are wider than literal types like `"SAVE"`. Use `as const` to prevent unintended widening.
- **Excess Property Checks**: TypeScript only checks for extra properties on *fresh* object literals. Assigning an object to a variable bypasses this check.
- **Hydration & Date**: `JSON.stringify` converts `Date` to `string`. Ensure types reflect this transformation when sending data over the wire.

## Verification Checklist
- [ ] `"strict": true` is verified in `tsconfig.json`.
- [ ] `any` usage is zero (verify with `@typescript-eslint/no-explicit-any`).
- [ ] Every `switch` statement on a union has an exhaustiveness check.
- [ ] All external data inputs are parsed and validated at the boundary.
