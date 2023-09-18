from app.server.database.database_connection import tasks
from app.server.models.tasks import TasksSchema

# Create the necessary endpoints to handle CRUD operations for tasks (Create, Read, Update, Delete).

# Create task
async def create_task(task: TasksSchema):
    try:
        new_task = await tasks.insert_one(tasks)
        get_new_task = await tasks.find_one(new_task.inserted_id)
        return get_new_task
    except Exception as e:
        return {"Error_message":str(e)}    
# Get one task
# Get all tasks
# Update one task
# Delete one task
# Delete all tasks