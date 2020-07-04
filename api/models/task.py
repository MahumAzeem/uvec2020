from typing import List, Optional
from pydantic import BaseModel

class Task(BaseModel):
   task_id: int = None
   title: str
   description: str = None
   priority: str = None
   status: str = None
   creator: int #employee id
   assigned_to: List[int] = None
   completion_time: int = None
   blocks_tasks: List[int]=None
   blocked_by: List[int] = None



