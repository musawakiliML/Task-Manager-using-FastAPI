from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def task_app():
   content = {"Message": "Your Task Manager for Daily Productivity...."}
   
   return JSONResponse(content=content, status_code=status.HTTP_200_OK)