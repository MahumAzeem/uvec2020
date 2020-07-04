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
    for i in employees:
        e = Employee(**i)
        employeeCounts[e.id] = 0
        scheduledTasks[e.id] = []
    
    for i in tasks:
        t = Task(**i)
        completion[t.id] = "N"


    while(tasks):
        for i in tasks:
            t = Task(**i)

            if len(t.preReqTasks) == 0:
                id = min(employeeCounts, key=employeeCounts.get)
                print(t.id, t.completionTime)
                scheduledTasks[id].append(t.id)
                employeeCounts[id] += t.completionTime
                completion[t.id] = "C"
                tasks.remove(i)
            for x, j in enumerate(t.preReqTasks):
                if completion[j] != "C":
                    break
                if x == len(t.preReqTasks)-1:
                    print(t.id, t.completionTime)
                    id = min(employeeCounts, key=employeeCounts.get)
                    scheduledTasks[id].append(t.id)
                    employeeCounts[id] += t.completionTime
                    completion[t.id] = "C"
                    tasks.remove(i)
    print(scheduledTasks)


if __name__ == "__main__" :
    addEmployee(employee_data)
    addTask(task1_data)
    taskOptimization()

