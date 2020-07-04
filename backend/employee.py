#/usr/bin/python3
from typing import List
from pydantic import BaseModel

# this list will be db when ready
employees = [
    {'id': '1', 'name': 'Smith Man'},
    {'id': '2', 'name': 'Hello Yo'}
]

class Employee(BaseModel):
    id: int
    name: str
    tasksAssigned: List[int] = []

def addEmployee(e):
    employees.append(e)

def getEmployees():
    return employees

employee_data = {
    'id': '3',
    'name': 'Jane Smith',
    'tasksAssigned': [1]
}