from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import datetime


class TasksSchema(BaseModel):
   name: str = Field(...)
   description: str = Field(...)
   status: str = Field(...)
   priority: str = Field(...)
   due_date: Union[datetime, None] = None
   created_time: Union[datetime, None] = None
   updated_time: Optional[str]

   class Config:
      json_schema_extra = {
         "example": [
            {
               "name":"Read a Book",
               "description":"Read a book on entreprenurship for 2 hours",
               "status":"completed",
               "priority":"p1",
               "due_date": "2023-09-10T23:23:35.403+00:00",
               "created_at":"2023-09-10T23:23:35.403+00:00",
               "updated_at":"2023-09-10T23:23:35.403+00:00"
            }
         ]
      }

