# Hello API Python

A minimal Flask API used by the repository labs.

## Endpoints

```text
GET /
GET /health
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:8000
```

## Run tests

```bash
pytest
```
