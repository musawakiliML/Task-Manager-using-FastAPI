from fastapi import APIRouter, status, HTTPException, Form, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime, time, timedelta
from typing import Annotated, Any

from app.server.database.crud import (
    create_task_db,
    get_single_task_db
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
    get_task = await get_single_task_db(id)
    
    try:
        if get_task:
            response =
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
