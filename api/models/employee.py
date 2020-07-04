from typing import List, Optional
from pydantic import BaseModel

class Employee(BaseModel):
    employee_id: int
    name: str
    tasks_assigned: List[int] = None
    tasks_created: List[int] = None

    @classmethod
    def assign_task(self, task_id:int):
        seld.emp_id = 
