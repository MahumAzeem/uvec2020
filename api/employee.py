from typing import List, Optional
from pydantic import BaseModel

class Employee(BaseModel):
    task_id: int
    name: str
    tasks_assigned: List[int]
    tasks_created: List[int]