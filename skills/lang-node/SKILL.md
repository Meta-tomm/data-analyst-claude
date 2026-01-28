---
name: lang-node
description: "Use when writing Node.js. Express/Fastify, streams, worker threads, fs/path, npm best practices."
---

# Node.js

Best practices for Node.js backend development.

## HTTP Frameworks

### Express
```javascript
import express from 'express';
const app = express();
app.use(express.json());

app.get('/api/users/:id', async (req, res, next) => {
    try {
        const user = await getUser(req.params.id);
        if (!user) return res.status(404).json({ error: 'Not found' });
        res.json(user);
    } catch (err) { next(err); }
});

// Error handler
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Internal error' });
});
```

### Fastify
```javascript
import Fastify from 'fastify';
const app = Fastify({ logger: true });

app.get('/api/users/:id', {
    schema: {
        params: { type: 'object', properties: { id: { type: 'string' } } },
        response: { 200: UserSchema }
    }
}, async (req) => {
    return getUser(req.params.id);
});
```

## File System
```javascript
import { readFile, writeFile, mkdir } from 'fs/promises';
import { join, resolve } from 'path';

const data = await readFile(join(process.cwd(), 'data.json'), 'utf-8');
await mkdir('output', { recursive: true });
await writeFile('output/result.json', JSON.stringify(data, null, 2));
```

## Streams (Large Data)
```javascript
import { createReadStream, createWriteStream } from 'fs';
import { pipeline } from 'stream/promises';
import { Transform } from 'stream';

const transform = new Transform({
    objectMode: true,
    transform(chunk, enc, cb) { cb(null, process(chunk)); }
});

await pipeline(
    createReadStream('input.csv'),
    csvParser(),
    transform,
    createWriteStream('output.csv')
);
```

## Worker Threads (CPU-intensive)
```javascript
import { Worker, isMainThread, parentPort, workerData } from 'worker_threads';

if (isMainThread) {
    const worker = new Worker(new URL(import.meta.url), { workerData: { task: 'heavy' } });
    worker.on('message', result => console.log(result));
} else {
    const result = heavyComputation(workerData);
    parentPort.postMessage(result);
}
```

## Environment & Config
```javascript
const config = {
    port: parseInt(process.env.PORT || '3000'),
    dbUrl: process.env.DATABASE_URL,
    nodeEnv: process.env.NODE_ENV || 'development',
};
```

## Anti-Patterns
| Bad | Good |
|-----|------|
| `require()` | `import` (ESM) |
| Sync fs operations | `fs/promises` |
| `process.exit()` in lib | Throw errors |
| No error handling | try/catch + error middleware |
| Global state | Dependency injection |

## Language

Respond in the same language as the user.
