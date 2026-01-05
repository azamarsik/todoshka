from database import TASKS
import models
from http import HTTPStatus
import schemas
import datetime
from fastapi import APIRouter

router = APIRouter()

@router.post("/tasks", status_code=HTTPStatus.CREATED)
async def create_tasks(task: schemas.TaskCreate):
    new_task = models.Task(
        id = len(TASKS) + 1,
        title = task.title,
        description = task.description,
        is_completed = task.is_completed,
        created_at = datetime.datetime.now(),
        updated_at = datetime.datetime.now(),
    )
    TASKS.append(new_task)
    return {
        "id": new_task.id,
        "title": new_task.title,
        "description": new_task.description,
        "is_completed": new_task.is_completed,
        "created_at": new_task.created_at,
        "updated_at": new_task.updated_at,
    }