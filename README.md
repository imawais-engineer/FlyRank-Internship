# Task API - FlyRank Backend W2 A1

A small CRUD API that manages a to-do list. Built with FastAPI.
Data lives only in memory - restarting the server clears new tasks.

## How to install & run

pip install -r requirements.txt
uvicorn main:app --reload --port 8000

Open:
- API: http://localhost:8000/
- Swagger UI: http://localhost:8000/docs
- Health: http://localhost:8000/health

## Endpoints
| Method | Path | Description | Status |
| GET | / | API info | 200 |
| GET | /health | Health | 200 |
| GET | /tasks | List all?done=true & search=milk | 200 |
| GET | /tasks/{id} | Get one | 200, 404 |
| POST | /tasks | Create {title} | 201, 400 |
| PUT | /tasks/{id} | Update title/done | 200, 400, 404 |
| DELETE | /tasks/{id} | Delete | 204, 404 |
| GET | /stats | Stats | 200 |
| POST | /reset | Reset to 3 | 200 |

## curl example
curl -i http://localhost:8000/tasks
curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{"title":"Buy milk"}'

## Example output
HTTP/1.1 201 Created
{"id":4,"title":"Buy milk","done":false}

## Mortality experiment
Create tasks, restart server (Ctrl+C then uvicorn again), GET /tasks -> tasks gone because in-memory list is in RAM.

## AI vs me
To be added in Stage 7.
