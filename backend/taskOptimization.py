#/usr/bin/python3
from typing import List
from pydantic import BaseModel
from employee import * 
from task import *

def taskOptimization():
    employees = []
    employees.extend(getEmployees())
    for i in employees:
        e = Employee(**i)
        print(e.dict())



if __name__ == "__main__" :
    print("hi")
    task = Task(**task1_data)
    addEmployee(employee_data)
    taskOptimization()

