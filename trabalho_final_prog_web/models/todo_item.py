from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class TodoItemStatus(str, Enum):
    pending = "pending"
    doing = "doing"
    done = "done"


class TodoItemCreationBody(BaseModel):
    project_id: int
    name: str
    description: str
    due_date: datetime

    class Config:
        extra = "forbid"


class TodoItemUpdateBody(BaseModel):
    name: str
    description: str
    status: TodoItemStatus
    due_date: datetime
    project_id: int

    class Config:
        extra = "forbid"
