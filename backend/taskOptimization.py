#/usr/bin/python3
from typing import List
from pydantic import BaseModel
from employee import * 
from task import *



def taskOptimization():
    employees = []
    employeeCounts = {}
    tasks = []
    scheduledTasks = {}
    
    employees.extend(getEmployees())
    numEmployees = len(employees)
    tasks.extend(getTasks())
    numTasks = len(tasks)
    completion = {}

    # set all employees with no tasks
    for i in employees:
        e = Employee(**i)
        employeeCounts[e.id] = 0
        scheduledTasks[e.id] = []
    
    # set all task ids as incomplete
    for i in tasks:
        t = Task(**i)
        completion[t.id] = "N"

#   sort task by priority so the ones higher get served first if available
    tasks.sort(key = getPriority, reverse=True)

    # for task in tasks:
    #     print(Task(**task).id, Task(**task).priority)


    while(tasks):
        for i in tasks:
            t = Task(**i)
            #  if no tasks are blocking current task, schedule it
            if len(t.preReqTasks) == 0:
                id = min(employeeCounts, key=employeeCounts.get)
                print(t.id, t.completionTime)
                scheduledTasks[id].append(t.id)
                employeeCounts[id] += t.completionTime
                completion[t.id] = "C"
                tasks.remove(i)
            # if all tasks blocking current task are complete, schedule it
            for x, j in enumerate(t.preReqTasks):
                if completion[j] != "C":
                    break
                if x == len(t.preReqTasks)-1:
                    print(t.id, t.completionTime)
                    id = min(employeeCounts, key=employeeCounts.get)
                    scheduledTasks[id].append(t.id)
                    employeeCounts[id] += t.completionTime
                    # if len(t.tasksBlocked) > 0:

                    completion[t.id] = "C"
                    tasks.remove(i)
    print(scheduledTasks)


def getPriority(elem):
    return Task(**elem).priority


if __name__ == "__main__" :
    addEmployee(employee_data)
    addTask(task1_data)
    taskOptimization()

