from enum import Enum

from pydantic import BaseModel


class ProjectStatus(str, Enum):
    pending = "pending"
    doing = "doing"
    done = "done"


class ProjectCreationBody(BaseModel):
    name: str
    description: str

    class Config:
        extra = "forbid"


class ProjectUpdateBody(BaseModel):
    name: str
    description: str
    status: ProjectStatus

    class Config:
        extra = "forbid"
