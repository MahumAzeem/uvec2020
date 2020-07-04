"""
Main server file for the API.
For request/response format specification, see api_spec.py.
See README for running instructions.
"""
import importlib
import json

from fastapi import FastAPI, HTTPException, Path, Query

from models.task import Task
from models.employee import Employee
#from storage import database

app = FastAPI()

@app.get("/all_tasks")
async def get_all_tasks():
    results = {1,2,3}
        #get tasks from db, filler data rn

    return results

@app.get("/task/{id}")
async def get_task(id: int) -> Task:
    """
    GET route for getting the a specific task.

    Args:
        id: The id of the task required.

    Returns:
        A JSON response contaning a task object.
    """
    #example task:
    task = Task(
        task_id= 1,
        title="Example Task",
        creator= 21
    )
    return task

@app.get("/employee/{id}")
async def get_employee(id: int):
    return null

@app.get("/")
async def root():
    """
    Root route. Currently just responds to a GET request with a message.
    Useful for testing that your server is working; will require a
    different response before deployment.
    """
    return {"message": "Welcome to Kira"}