from typing import List
from pydantic import BaseModel
from models.employee import * 
from models.task import *
from db_setup import *

employees = []
tasks = []

def addEmployee(e):
    employees.append(e)

def addTask(task):
    tasks.append(task)


def taskOptimization():
    employees = []
    employeeCounts = {}
    tasks = []
    scheduledTasks = {}

    
    e = getEmployees()
    if e is not None:
        for i in e:
            em = {'employee_id': i[0], 'name': i[1], 'tasks_assigned': i[2], 'tasks_created': i[3]}

    
    numEmployees = len(employees)
    # tasks.extend(getTasks())
    if t is not None:
        for i in t:
            ta = {'task_id': i[0], 'title': i[1], 'description': i[2], 'priority': i[3], 'status': i[4], 'assigned_to': i[4].split(' '), 'completion_time': i[5], 'blocks_task': i[6].split(' '), 'blocked_by': i[7].split(' ')}

    numTasks = len(tasks)
    completion = {}

    # set all employees with no tasks
    # for i in employees:
    #     e = Employee(**i)
    #     # employeeCounts[e.employee_id] = 0
    #     # scheduledTasks[e.employee_id] = []
    
    # set all task ids as incomplete
    for i in tasks:
        t = Task(**i)
        completion[t.task_id] = "N"

#   sort task by priority so the ones higher get served first if available
    tasks.sort(key = getPriority, reverse=True)

    # for task in tasks:
    #     print(Task(**task).id, Task(**task).priority)


    while(tasks):
        for i in tasks:
            t = Task(**i)
            #  if no tasks are blocking current task, schedule it
            if not t.blocked_by:
                print(t.task_id, t.completion_time)
                completion[t.task_id] = "C"
                tasks.remove(i)
            # if all tasks blocking current task are complete, schedule it
            if t.blocked_by:
                for x, j in enumerate(t.blocked_by):
                    if completion[j] != "C":
                        break
                    if x == len(t.blocked_by)-1:
                        print(t.id, t.completion_time)
                        completion[t.task_id] = "C"
                        tasks.remove(i)
    # print(scheduledTasks)


def getPriority(elem):
    return Task(**elem).priority

task1 = {'task_id': '1', 'title': 'Task 1', 'description': 'A description', 'priority': 'MED', 'status': 'In Progress', 'creator': '1', 'assigned_to': [1,2], 'completion_time': 4}
employee1 = {'employee_id': '1', 'name': 'John Smith'}

if __name__ == "__main__" :
    addEmployee(employee1)
    addTask(task1)
    taskOptimization()