from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI(title="Task API", version="1.0")

tasks = [
    {"id": 1, "title": "Learn HTTP methods", "done": False},
    {"id": 2, "title": "Build first CRUD API", "done": False},
    {"id": 3, "title": "Test in Swagger UI", "done": True},
]

def find_task(task_id: int):
    return next((t for t in tasks if t["id"] == task_id), None)

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
