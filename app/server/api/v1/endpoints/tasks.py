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
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TasksSchema)
async def create_task(name: str=Form(defaut="Reading"), description: str=Form(default="read 50 pages of steal like an artist"), task_status: str=Form(default="completed"), priority: str=Form(default="p1"), due_date: Annotated[datetime | None, Body()]=Form()):
    created_date = ""
    # Create task function
    schema = TasksSchema(
        name=name,
        description=description,
        status=task_status,
        priority=priority,
        due_date=due_date
    )
    new_task = await create_task(schema)

    response = jsonable_encoder(new_task)

    return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)