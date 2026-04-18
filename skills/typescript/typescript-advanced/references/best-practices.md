# Advanced TypeScript Patterns & Best Practices

This guide focuses on modeling your domain using advanced type systems to ensure runtime safety and catch bugs at compile-time.

## 1. Discriminated Unions (Modeling State)
Never use multiple optional properties to represent different states. Use a discriminant property.

### ❌ Bad
```typescript
interface ApiResponse {
  data?: User;
  error?: string;
  isLoading: boolean;
}
```

### ✅ Good
```typescript
type ApiResponse<T> =
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; error: string };

function handle(res: ApiResponse<User>) {
  if (res.status === "success") {
    console.log(res.data.name); // Type-safe
  }
}
```

## 2. Generic Constraints
Use generics to create reusable logic while maintaining strict boundaries.

```typescript
// Good: Using 'extends' to ensure T has a 'length' property
function getLength<T extends { length: number }>(item: T): number {
  return item.length;
}

getLength("hello"); // OK
getLength([1, 2]); // OK
getLength(123);     // Error: number doesn't have length
```

## 3. Utility Types (DRY Principle)
Avoid duplicating interface definitions. Transform them instead.

- **Pick**: When you only need a few fields.
- **Omit**: When you want everything *except* a few fields.
- **Partial**: For update functions.

```typescript
interface Product {
  id: string;
  name: string;
  price: number;
}

// Good: Reusing the Product type for updates
type ProductUpdate = Partial<Omit<Product, "id">>;

function updateProduct(id: string, update: ProductUpdate) {
  // id cannot be updated
}
```

## 4. Exhaustiveness Checking
Ensure that your `switch` statements cover every possible branch.

```typescript
function assertNever(x: never): never {
  throw new Error("Unexpected object: " + x);
}

function handleState(res: ApiResponse<User>) {
  switch (res.status) {
    case "success": return "Done";
    case "error": return "Error";
    case "loading": return "Waiting";
    default:
      return assertNever(res); // Error if a newly added status isn't handled
  }
}
```
