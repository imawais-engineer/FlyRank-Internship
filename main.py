from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Task API", version="1.0", description="FlyRank Backend W2 A1 - Task CRUD API")

tasks = [
    {"id": 1, "title": "Learn HTTP methods", "done": False},
    {"id": 2, "title": "Build first CRUD API", "done": False},
    {"id": 3, "title": "Test in Swagger UI", "done": True},
]

def get_next_id():
    return max((t["id"] for t in tasks), default=0) + 1
def find_task(task_id: int):
    return next((t for t in tasks if t["id"] == task_id), None)

class TaskCreate(BaseModel):
    title: Optional[str] = None
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

@app.get("/", summary="API info")
def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}
@app.get("/health", summary="Health check")
def health():
    return {"status": "ok"}
@app.get("/tasks", summary="List all tasks")
def list_tasks(done: Optional[bool] = None, search: Optional[str] = None):
    result = tasks
    if done is not None:
        result = [t for t in result if t["done"] == done]
    if search:
        result = [t for t in result if search.lower() in t["title"].lower()]
    return result
@app.get("/tasks/{task_id}", summary="Get single task")
def get_task(task_id: int):
    task = find_task(task_id)
    if not task:
        return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})
    return task
@app.post("/tasks", status_code=201, summary="Create a new task")
def create_task(payload: TaskCreate):
    if not payload.title or not payload.title.strip():
        return JSONResponse(status_code=400, content={"error": "Title is required and cannot be empty"})
    new_task = {"id": get_next_id(), "title": payload.title.strip(), "done": False}
    tasks.append(new_task)
    return new_task
@app.put("/tasks/{task_id}", summary="Update a task")
def update_task(task_id: int, payload: TaskUpdate):
    task = find_task(task_id)
    if not task:
        return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})
    if payload.title is None and payload.done is None:
        return JSONResponse(status_code=400, content={"error": "Provide title and/or done to update"})
    if payload.title is not None:
        if not payload.title.strip():
            return JSONResponse(status_code=400, content={"error": "Title cannot be empty"})
        task["title"] = payload.title.strip()
    if payload.done is not None:
        task["done"] = payload.done
    return task
@app.delete("/tasks/{task_id}", status_code=204, summary="Delete a task")
def delete_task(task_id: int):
    task = find_task(task_id)
    if not task:
        return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})
    tasks.remove(task)
    return Response(status_code=204)
@app.get("/stats", summary="Task stats")
def get_stats():
    total = len(tasks)
    done_count = sum(1 for t in tasks if t["done"])
    return {"total": total, "done": done_count, "open": total - done_count}
@app.post("/reset", summary="Reset to 3 example tasks")
def reset_tasks():
    global tasks
    tasks = [
        {"id": 1, "title": "Learn HTTP methods", "done": False},
        {"id": 2, "title": "Build first CRUD API", "done": False},
        {"id": 3, "title": "Test in Swagger UI", "done": True},
    ]
    return tasks
