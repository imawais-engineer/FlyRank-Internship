from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Task API", version="1.0")

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

@app.get("/")
def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}
@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/tasks")
def list_tasks():
    return tasks
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = find_task(task_id)
    if not task:
        return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})
    return task

@app.post("/tasks", status_code=201)
def create_task(payload: TaskCreate):
    if not payload.title or not payload.title.strip():
        return JSONResponse(status_code=400, content={"error": "Title is required and cannot be empty"})
    new_task = {"id": get_next_id(), "title": payload.title.strip(), "done": False}
    tasks.append(new_task)
    return new_task
