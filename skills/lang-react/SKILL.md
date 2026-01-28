---
name: lang-react
description: "Use when writing React. Hooks patterns, state management, performance optimization, testing, Server Components."
---

# React

Best practices for React development.

## Hooks Patterns

### State
```tsx
const [items, setItems] = useState<Item[]>([]);
const [status, setStatus] = useState<'idle' | 'loading' | 'error'>('idle');

// Reducer for complex state
const [state, dispatch] = useReducer(reducer, initialState);
```

### Effects
```tsx
// Data fetching
useEffect(() => {
    const controller = new AbortController();
    fetchData({ signal: controller.signal }).then(setData).catch(console.error);
    return () => controller.abort();
}, [id]);
```

### Custom Hooks
```tsx
function useDebounce<T>(value: T, delay: number): T {
    const [debounced, setDebounced] = useState(value);
    useEffect(() => {
        const timer = setTimeout(() => setDebounced(value), delay);
        return () => clearTimeout(timer);
    }, [value, delay]);
    return debounced;
}

function useLocalStorage<T>(key: string, initial: T) {
    const [value, setValue] = useState<T>(() => {
        const stored = localStorage.getItem(key);
        return stored ? JSON.parse(stored) : initial;
    });
    useEffect(() => localStorage.setItem(key, JSON.stringify(value)), [key, value]);
    return [value, setValue] as const;
}
```

## Performance

### Memoization (use sparingly, measure first)
```tsx
const expensive = useMemo(() => computeExpensive(data), [data]);
const handler = useCallback((id: string) => selectItem(id), [selectItem]);
const Row = React.memo(({ item }: { item: Item }) => <div>{item.name}</div>);
```

### Code Splitting
```tsx
const Dashboard = lazy(() => import('./Dashboard'));
<Suspense fallback={<Spinner />}><Dashboard /></Suspense>
```

### Virtual Lists (large data)
```tsx
import { FixedSizeList } from 'react-window';
<FixedSizeList height={600} width={400} itemSize={35} itemCount={items.length}>
    {({ index, style }) => <div style={style}>{items[index].name}</div>}
</FixedSizeList>
```

## State Management

### Context (simple shared state)
```tsx
const ThemeContext = createContext<Theme>('light');
const useTheme = () => useContext(ThemeContext);
```

### Zustand (recommended for medium complexity)
```tsx
import { create } from 'zustand';
const useStore = create<State>((set) => ({
    items: [],
    addItem: (item) => set((s) => ({ items: [...s.items, item] })),
}));
```

### React Query (server state)
```tsx
const { data, isLoading } = useQuery({
    queryKey: ['users', id],
    queryFn: () => fetchUser(id),
});
```

## Server Components (Next.js App Router)
```tsx
// Server Component (default)
async function UserList() {
    const users = await db.users.findMany();
    return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}

// Client Component
'use client';
function SearchBar() {
    const [query, setQuery] = useState('');
    return <input value={query} onChange={e => setQuery(e.target.value)} />;
}
```

## Testing
```tsx
import { render, screen, fireEvent } from '@testing-library/react';

test('renders and handles click', () => {
    render(<Button onClick={mockFn}>Click</Button>);
    fireEvent.click(screen.getByText('Click'));
    expect(mockFn).toHaveBeenCalledOnce();
});
```

## Anti-Patterns
| Bad | Good |
|-----|------|
| Props drilling >3 levels | Context or state lib |
| useEffect for derived state | useMemo or compute inline |
| Index as key | Stable unique ID |
| Premature memo | Measure first |
| `any` in props | Strict TypeScript types |

## Language

Respond in the same language as the user.
