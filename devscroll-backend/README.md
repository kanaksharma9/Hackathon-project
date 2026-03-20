# DevScroll Backend

Backend API for DevScroll — an Instagram-style learning feed for CS students.

Stack: FastAPI + SQLite + Google Gemini API.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up environment variables:
   Copy `.env.example` to `.env` and add your Gemini key.
   ```bash
   cp .env.example .env
   # Edit .env and set GEMINI_API_KEY
   ```

## Run

Run the development server locally:
```bash
uvicorn main:app --reload --port 8000
```

API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## Endpoints

### 1. Create a Feed Session
**Endpoint:** `POST /session`

**Curl Example:**
```bash
curl -X POST http://localhost:8000/session \
     -H "Content-Type: application/json" \
     -d '{"chips": ["React", "DSA", "AI"]}'
```

### 2. Save a Reflection
**Endpoint:** `POST /reflect`

**Curl Example:**
```bash
curl -X POST http://localhost:8000/reflect \
     -H "Content-Type: application/json" \
     -d '{"session_id": "uuid-string-here", "card_index": 5, "reflection_text": "MapReduce splits data..."}'
```

### 3. Health Check
**Endpoint:** `GET /health`

**Curl Example:**
```bash
curl http://localhost:8000/health
```
