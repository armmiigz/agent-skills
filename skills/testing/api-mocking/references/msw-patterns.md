# API Mocking Patterns (MSW)

This reference provides standard patterns for mocking APIs using **Mock Service Worker (MSW)** to enable isolated development and testing.

## 1. Standard CRUD Handlers
Use these patterns to mock typical RESTful endpoints.

```typescript
import { http, HttpResponse, delay } from 'msw';

export const handlers = [
  // Mock GET: Fetching a list
  http.get('/api/items', async () => {
    await delay(500); // Simulate realistic network delay
    return HttpResponse.json([
      { id: '1', name: 'Mock Item 1' },
      { id: '2', name: 'Mock Item 2' },
    ]);
  }),

  // Mock POST: Successful creation
  http.post('/api/items', async ({ request }) => {
    const newItem = await request.json();
    return HttpResponse.json(newItem, { status: 201 });
  }),
];
```

## 2. Simulating Failure States
Crucial for verifying that the UI handles errors gracefully.

```typescript
// Mock 500 Internal Server Error
http.get('/api/error-trigger', () => {
  return new HttpResponse(null, { status: 500 });
}),

// Mock 404 Not Found
http.get('/api/missing-item', () => {
  return new HttpResponse(null, { status: 404 });
})
```

## 3. Advanced Scenarios
- **Empty States**: Return an empty array `[]` to test empty views.
- **Large Data**: Use a loop to generate 100+ items to test virtualization or pagination UI.
- **Authentication**: Check for `Authorization` headers and return 401 if missing.
