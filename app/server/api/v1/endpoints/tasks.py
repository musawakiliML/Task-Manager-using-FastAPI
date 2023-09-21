from fastapi import APIRouter, status, HTTPException, Form, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime, time, timedelta
from typing import Annotated, Any, List

from app.server.database.crud import (
    create_task_db,
    get_single_task_db,
    get_all_tasks_db
)
from app.server.models.tasks import (
    TasksSchema
)

router = APIRouter()

# Create task route
@router.post("/", response_model=TasksSchema, response_description="Creating A Task")
async def create_task(name: Annotated[str, Form()],
                      description: Annotated[str, Form()],
                      task_status: Annotated[str, Form()],
                      priority: Annotated[str, Form()],
                      due_date: Annotated[str, Form()]) -> Any:
    try:
        created_at = datetime.utcnow()
        # Create task function
        task = TasksSchema(
            name=name,
            description=description,
            task_status=task_status,
            priority=priority,
            due_date=due_date,
            created_at=created_at,
            updated_at=None
        )
        new_task = await create_task_db(task)
        
        response = {
            "id": str(new_task["_id"]),
            "message": "Task Created Successfully"
        }
        response = jsonable_encoder(response)

        return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

# Get Single Task
@router.get("/{id}", response_model=TasksSchema, response_description="Get Single Task")
async def get_single_task(id: str):
    try:
        get_task = await get_single_task_db(id)
        if get_task:
            response = TasksSchema(
                name=get_task["name"],
                description=get_task["description"],
                task_status=get_task["task_status"],
                priority=get_task["priority"],
                due_date=get_task["due_date"],
                created_at=get_task["created_at"],
                updated_at=get_task["updated_at"]
            )
            response = jsonable_encoder(response)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# Get all Tasks
@router.get("/", response_model=List[TasksSchema], response_description="Get all Tasks")
async def get_all_tasks():
    all_tasks_list = []
    try:
        get_all_tasks = await get_all_tasks_db()
        if get_all_tasks:
            for task in get_all_tasks:
                task_data = TasksSchema(
                    name=task["name"],
                    description=task["description"],
                    task_status=task["task_status"],
                    priority=task["priority"],
                    due_date=task["due_date"],
                    created_at=task["created_at"],
                    updated_at=task["updated_at"]
                )
                all_tasks_list.append(task_data)
            response = jsonable_encoder(all_tasks_list)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))