"""
Main server file for the API.
For request/response format specification, see api_spec.py.
See README for running instructions.
"""
import importlib
import json
import db_setup as db

from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.middleware.cors import CORSMiddleware

from models.task import Task
from models.employee import Employee
#from storage import database

app = FastAPI()
db.init()

def application(environ, start_response):
  if environ['REQUEST_METHOD'] == 'OPTIONS':
    start_response(
      '200 OK',
      [
        ('Content-Type', 'application/json'),
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Headers', 'Authorization, Content-Type'),
        ('Access-Control-Allow-Methods', 'POST'),
      ]
    )
    return ''

@app.get("/all_tasks")
async def get_all_tasks():
    results = db.getTasks()
    return results

@app.get("/task/{id}")
async def get_task(id: int) -> Task:
    task = db.getTask(1)
    return task
      
@app.post("/task")
async def create_task(task: Task):
    task.task_id = db.createTask(task)[0][0]
    return task

# @app.delete("/task/{id}")
# async def delete_task(id: int):
#     return OK

@app.get("/employee/{id}")
async def get_employee(id: int):
    new = Employee(
        name = "Mahum",
        tasks_assigned = {1,2,3},
        tasks_created = {1}
    )
    return new

@app.put("employee/{id}")
async def update_employee(employee: Employee):
    employee.update(id)
    return employee   

@app.get("/all_employees")
async def get_all_employees():
    return []

@app.post("/employee")
async def create_employee(employee: Employee):
    db.createEmployee(Employee)
    return employee

 

@app.get("/")
async def root():
    """
    Root route. Currently just responds to a GET request with a message.
    Useful for testing that your server is working; will require a
    different response before deployment.
    """
    return {"message": "Welcome to Kira"}