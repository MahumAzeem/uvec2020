#/usr/bin/python3
from typing import List
from pydantic import BaseModel
from employee import * 
from task import *



def taskOptimization():
    employees = []
    tasks = []
    
    employees.extend(getEmployees())
    numEmployees = len(employees)
    tasks.extend(getTasks())
    numTasks = len(tasks)
    completion = {}
    for i in employees:
        e = Employee(**i)
    
    for i in tasks:
        t = Task(**i)
        completion[t.id] = "N"

    # tasks.sort(key=lambda x.id)

    while(tasks):
        for i in tasks:
            t = Task(**i)

            if len(t.preReqTasks) == 0:
                print(t.id, t.completionTime)
                completion[t.id] = "C"
                tasks.remove(i)
            for x, j in enumerate(t.preReqTasks):
                if completion[j] != "C":
                    break
                if x == len(t.preReqTasks)-1:
                    print(t.id, t.completionTime)
                    completion[t.id] = "C"
                    tasks.remove(i)



if __name__ == "__main__" :
    # task = Task(**task1_data)
    addEmployee(employee_data)
    addTask(task1_data)
    taskOptimization()

