from app.server.database.database_connection import tasks
from app.server.models.tasks import TasksSchema
from bson.objectid import ObjectId

# Create the necessary endpoints to handle CRUD operations for tasks (Create, Read, Update, Delete).

# Create task
async def create_task_db(task: TasksSchema):
    task = task.model_dump()
    try:
        print("Inside create task function")
        new_task = await tasks.insert_one(task)
        get_new_task = await tasks.find_one({"_id": new_task.inserted_id})
        return get_new_task
    except Exception as e:
        return {"Error_message":str(e)}

# Get one task
async def get_single_task_db(id: str):
    try:
        task = await tasks.find_one({"_id":ObjectId(id)})
        if task:
            return task
    except Exception as e:
        return {"Error_message": str(e)}

# Get all tasks
async def get_all_tasks_db():
    try:
        get_all_tasks = await tasks.find()
        if get_all_tasks:
            return get_all_tasks
    except Exception as e:
        return {"Error_message": str(e)}
# Update one task
# Delete one task
# Delete all tasks