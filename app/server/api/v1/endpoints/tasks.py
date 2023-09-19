from fastapi import APIRouter, status, HTTPException, Form, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime, time, timedelta
from typing import Annotated

from app.server.database.crud import (
    create_task
)
from app.server.models.tasks import (
    TasksSchema
)

router = APIRouter()

# Create task route
@router.post("/", response_model=TasksSchema, response_description="Creating A Task")
async def create_task(name: str=Form(default="Reading"), description: str=Form(default="read 50 pages of steal like an artist"), task_status: str=Form(default="completed"), priority: str=Form(default="p1"), task_due_date: str=Form(default="today")):
    try:
        created_date = datetime.utcnow()
        # due_date = datetime.strptime(due_date, '%Y-%m-%d')
        # print(due_date)
        # Create task function
        schema = TasksSchema(
            name=str(name),
            description=str(description),
            status=str(task_status),
            priority=str(priority),
            due_date=str(task_due_date),
            created_time=str(created_date),
            updated_time=None
        )
        print("Inside try before new task")
        new_task = await create_task(schema)
        
        print("After creating new task")

        response = jsonable_encoder(new_task)

        return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    