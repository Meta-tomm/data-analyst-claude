---
name: lang-javascript
description: "Use when writing JavaScript. ES2024+, functional patterns, async/await, Web APIs, performance."
---

# JavaScript

Best practices for modern JavaScript (ES2024+).

## Modern Syntax

```javascript
// Destructuring
const { name, age = 0, ...rest } = user;
const [first, ...others] = items;

// Optional chaining + nullish coalescing
const city = user?.address?.city ?? 'Unknown';

// Structured clone (deep copy)
const copy = structuredClone(original);

// Object.groupBy (ES2024)
const grouped = Object.groupBy(items, item => item.category);

// Array.at
const last = arr.at(-1);

// Promise.withResolvers (ES2024)
const { promise, resolve, reject } = Promise.withResolvers();
```

## Functional Patterns
```javascript
// Pipeline (compose)
const pipeline = (...fns) => x => fns.reduce((v, f) => f(v), x);
const transform = pipeline(normalize, validate, format);

// Immutable updates
const updated = { ...obj, key: newValue };
const withoutKey = (({ key, ...rest }) => rest)(obj);

// Map/Filter/Reduce
const totals = orders
    .filter(o => o.status === 'completed')
    .map(o => o.amount)
    .reduce((sum, amt) => sum + amt, 0);
```

## Async Patterns
```javascript
// Parallel
const [users, posts] = await Promise.all([fetchUsers(), fetchPosts()]);

// Sequential with for...of
for (const item of items) {
    await process(item);
}

// Concurrency limit
async function mapConcurrent(items, fn, limit = 5) {
    const results = [];
    for (let i = 0; i < items.length; i += limit) {
        const batch = items.slice(i, i + limit);
        results.push(...await Promise.all(batch.map(fn)));
    }
    return results;
}

// AbortController
const controller = new AbortController();
setTimeout(() => controller.abort(), 5000);
const res = await fetch(url, { signal: controller.signal });
```

## Performance
- Use `Map` over object for frequent add/delete
- Use `Set` for uniqueness checks
- Avoid blocking main thread (use Web Workers)
- Debounce user input (300ms), throttle scroll (100ms)
- Lazy load modules: `const mod = await import('./module.js')`

## Anti-Patterns
| Bad | Good |
|-----|------|
| `var` | `const` / `let` |
| `==` | `===` |
| `for (var i in arr)` | `for (const item of arr)` |
| `.then().catch()` | `async/await + try/catch` |
| `new Date()` for formatting | `Intl.DateTimeFormat` |

## Language

Respond in the same language as the user.
