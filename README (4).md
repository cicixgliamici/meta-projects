# Snippet — Flask Hello API

This file contains a minimal Flask API snippet you can reuse in labs.

## Example

```python
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({"message": "Hello from Software Delivery Lab!", "status": "ok"})


@app.get("/health")
def health():
    return jsonify({"service": "hello-api-python", "status": "healthy"})
```

## Notes

- Keep endpoints simple and predictable.
- Always provide a `/health` endpoint for CI/CD and monitoring.
