# Testing Patterns Reference

Guidelines and examples for writing robust tests using **Vitest** and **React Testing Library**.

## 1. Unit Testing (Logic)
Focus on pure functions and business logic.

```typescript
import { describe, it, expect } from 'vitest';
import { calculateTotal } from './utils';

describe('calculateTotal', () => {
  it('should sum items correctly', () => {
    const items = [{ price: 10 }, { price: 20 }];
    expect(calculateTotal(items)).toBe(30);
  });
});
```

## 2. Component Testing (UI)
Focus on user behavior and interactions.

```typescript
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

test('calls onClick when clicked', () => {
  const handleClick = vi.fn();
  render(<Button onClick={handleClick}>Click Me</Button>);
  
  fireEvent.click(screen.getByText(/click me/i));
  expect(handleClick).toHaveBeenCalledTimes(1);
});
```

## 3. Best Practices
- **TDD (Test-Driven Development)**: Write the test before the implementation.
- **Describe User Behavior**: Use `getByRole` or `getByText` instead of querying by internal classes or IDs.
- **Avoid Implementation Details**: Don't test private methods; test the public interface/result.
