# Task API – FlyRank Backend W2 A1

A simple CRUD API built with **FastAPI** that manages an in-memory to-do list.

> **Note:** Tasks are stored only in memory. Restarting the server resets the task list.

---

## Features

- ✅ Create tasks
- ✅ Read all tasks
- ✅ Read a single task
- ✅ Update tasks
- ✅ Delete tasks
- ✅ Swagger UI documentation
- ✅ Task filtering (`done=true`)
- ✅ Task searching (`search=...`)
- ✅ Statistics endpoint
- ✅ Reset endpoint

---

# Installation & Run

```bash
cd "W2 · A1 — Build your first CRUD API"

pip install -r requirements.txt

uvicorn main:app --reload --port 8000
```

The API will be available at:

- API Root: http://localhost:8000/
- Swagger UI: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

---

# API Endpoints

| Method | Endpoint | Description | Success |
|---------|----------|-------------|---------|
| GET | `/` | API information | 200 |
| GET | `/health` | Health check | 200 |
| GET | `/tasks` | List tasks (supports `done` and `search`) | 200 |
| GET | `/tasks/{id}` | Get one task | 200 / 404 |
| POST | `/tasks` | Create a task | 201 / 400 |
| PUT | `/tasks/{id}` | Update task | 200 / 400 / 404 |
| DELETE | `/tasks/{id}` | Delete task | 204 / 404 |
| GET | `/stats` | Task statistics | 200 |
| POST | `/reset` | Restore default tasks | 200 |

---

# Example Requests

List tasks

```bash
curl -i http://localhost:8000/tasks
```

Create a task

```bash
curl -i -X POST http://localhost:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Buy milk"}'
```

---

# Example Response

```http
HTTP/1.1 201 Created

{
  "id": 4,
  "title": "Buy milk",
  "done": false
}
```

---

# Swagger UI

FastAPI automatically generates interactive API documentation.

Open:

```
http://localhost:8000/docs
```

*(Insert your Swagger UI screenshot here.)*

---

# Mortality Experiment

Tasks are stored only in RAM.

If the server is restarted:

1. Create a few tasks.
2. Stop the server.
3. Start it again.
4. Call `GET /tasks`.

The newly created tasks disappear because no database or file storage is used. The application reloads the original in-memory list.

---

# AI vs Me

**Stage 7 (Optional)**

This section will compare a hand-written implementation with an AI-generated implementation after completing the optional assignment.

---

# Final curl Verification

```http
HTTP/1.1 200 OK
date: Thu, 23 Jul 2026 05:11:12 GMT
server: uvicorn
content-type: application/json

[
  {
    "id":1,
    "title":"Learn HTTP methods",
    "done":false
  },
  {
    "id":2,
    "title":"Build first CRUD API",
    "done":false
  },
  {
    "id":3,
    "title":"Test in Swagger UI",
    "done":true
  }
]

HTTP/1.1 201 Created

{
  "id":4,
  "title":"Buy milk",
  "done":false
}
```
