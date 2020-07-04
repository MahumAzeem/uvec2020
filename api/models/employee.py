from typing import List, Optional
from pydantic import BaseModel

class Employee(BaseModel):
    employee_id: int = None
    name: str
    tasks_assigned: List[int] = None
    tasks_created: List[int] = None

    # def save(self):
    #     return True
    
    # def update_employee(self, id):
    #     return True