# backend/api/self_evolution.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Router for self-evolution logic
router = APIRouter()

# Example data model for self-evolution tasks
class EvolutionTask(BaseModel):
    task_id: str
    description: str
    status: str  # e.g., "pending", "in-progress", "completed"
    progress: Optional[float] = 0.0  # Progress percentage (0-100)

# Example in-memory data store for self-evolution tasks
evolution_tasks = []

@router.get("/", response_model=List[EvolutionTask])
def get_all_evolution_tasks():
    """
    Retrieve all self-evolution tasks.
    """
    return evolution_tasks

@router.get("/{task_id}", response_model=EvolutionTask)
def get_evolution_task_by_id(task_id: str):
    """
    Retrieve a specific self-evolution task by its ID.
    """
    for task in evolution_tasks:
        if task.task_id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.post("/", response_model=EvolutionTask)
def create_evolution_task(task: EvolutionTask):
    """
    Create a new self-evolution task.
    """
    for existing_task in evolution_tasks:
        if existing_task.task_id == task.task_id:
            raise HTTPException(status_code=400, detail="Task ID already exists")
    evolution_tasks.append(task)
    return task

@router.put("/{task_id}", response_model=EvolutionTask)
def update_evolution_task(task_id: str, updated_task: EvolutionTask):
    """
    Update an existing self-evolution task by its ID.
    """
    for index, task in enumerate(evolution_tasks):
        if task.task_id == task_id:
            evolution_tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@router.patch("/{task_id}", response_model=EvolutionTask)
def update_task_progress(task_id: str, progress: float):
    """
    Update the progress of an existing self-evolution task by its ID.
    """
    if progress < 0 or progress > 100:
        raise HTTPException(status_code=400, detail="Progress must be between 0 and 100")
    for task in evolution_tasks:
        if task.task_id == task_id:
            task.progress = progress
            if progress == 100:
                task.status = "completed"
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/{task_id}")
def delete_evolution_task(task_id: str):
    """
    Delete a self-evolution task by its ID.
    """
    for index, task in enumerate(evolution_tasks):
        if task.task_id == task_id:
            del evolution_tasks[index]
            return {"message": f"Task {task_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
# Placeholder content for backend/api/self_evolution.py
