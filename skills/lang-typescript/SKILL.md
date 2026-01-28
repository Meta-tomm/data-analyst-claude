---
name: lang-typescript
description: "Use when writing TypeScript. Strict types, generics, utility types, Zod validation, async patterns."
---

# TypeScript

Best practices for TypeScript development.

## Strict Mode Always
```json
{ "compilerOptions": { "strict": true, "noUncheckedIndexedAccess": true } }
```

## Type Patterns

### Discriminated Unions
```typescript
type Result<T, E = Error> =
  | { success: true; data: T }
  | { success: false; error: E };
```

### Branded Types
```typescript
type UserId = string & { readonly __brand: 'UserId' };
const createUserId = (id: string): UserId => id as UserId;
```

### Utility Types
```typescript
Partial<T>       // All optional
Required<T>      // All required
Pick<T, K>       // Select keys
Omit<T, K>       // Remove keys
Record<K, V>     // Key-value map
ReturnType<F>    // Function return type
Awaited<T>       // Unwrap Promise
```

### Generic Constraints
```typescript
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}
```

## Zod Validation
```typescript
import { z } from 'zod';

const UserSchema = z.object({
    id: z.string().uuid(),
    email: z.string().email(),
    age: z.number().int().min(0).max(150),
    role: z.enum(['admin', 'user', 'viewer']),
});

type User = z.infer<typeof UserSchema>;

const result = UserSchema.safeParse(input);
if (result.success) { /* result.data is User */ }
```

## Async Patterns
```typescript
// Parallel
const [users, posts] = await Promise.all([fetchUsers(), fetchPosts()]);

// Error handling
const results = await Promise.allSettled(ids.map(fetchUser));
const successful = results.filter(r => r.status === 'fulfilled').map(r => r.value);

// Retry
async function withRetry<T>(fn: () => Promise<T>, retries = 3): Promise<T> {
    for (let i = 0; i < retries; i++) {
        try { return await fn(); }
        catch (e) { if (i === retries - 1) throw e; }
    }
    throw new Error('Unreachable');
}
```

## Anti-Patterns
| Bad | Good |
|-----|------|
| `any` | `unknown` then narrow |
| Type assertions `as T` | Type guards |
| `enum` | `const` object + `typeof` |
| `interface` for utility | `type` alias |

## Language

Respond in the same language as the user.
