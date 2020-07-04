#/usr/bin/python3
from typing import List
from pydantic import BaseModel

# will be a db
tasks = [
    {'id': '1', 'title': 'Task 1', 'description': 'A description', 'priority': 'MED', 'status': 'In Progress', 'creator': '1', 'assigned': [1,2], 'completionTime': 4},
    {'id': '2', 'title': 'Task 2', 'description': 'A description', 'priority': 'MED', 'status': 'In Progress', 'creator': '1', 'completionTime': 4}
]

class Task(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str
    creator: int
    assigned: List[int] = []
    completionTime: int
    preReqTasks: List[int] = [] 
    tasksBlocked: List[int] = [] 

def addTask(task):
    tasks.append(task)

def getTasks():
    return tasks


task1_data = {
    'id': '3',
    'title': 'Task 3',
    'description': 'A description',
    'priority': 'MED',
    'status': 'In Progress',
    'creator': '1',
    'assigned': [1,2],
    'completionTime': 4
}