from datetime import datetime

from sqlmodel import Column, DateTime, Field, Integer, SQLModel, text

from .project import ProjectStatus
from .todo_item import TodoItemStatus


# Definition of "project" table model using SQLModel
class Project(SQLModel, table=True):
    id: int = Field(
        sa_column=Column(
            Integer, primary_key=True, unique=True, index=True, autoincrement=True
        ),
        description="The primary key of the project table",
    )
    name: str = Field(index=True, max_length=255, description="The name of the project")
    description: str = Field(
        max_length=255, description="The description of the project"
    )
    status: ProjectStatus
    created_at: datetime = Field(
        sa_column=Column(DateTime, server_default=text("CURRENT_TIMESTAMP")),
        description="The timestamp when the project was created",
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime,
            server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        ),
        description="The timestamp when the project was last updated",
    )


# Definition of "todo_item" table model using SQLModel
class TodoItem(SQLModel, table=True):
    id: int = Field(
        sa_column=Column(
            Integer, primary_key=True, unique=True, index=True, autoincrement=True
        ),
        description="The primary key of the todo_item table",
    )
    name: str = Field(
        index=True, max_length=255, description="The name of the todo_item"
    )
    description: str = Field(
        max_length=255, description="The description of the todo_item"
    )
    status: TodoItemStatus
    due_date: datetime
    created_at: datetime = Field(
        sa_column=Column(DateTime, server_default=text("CURRENT_TIMESTAMP")),
        description="The timestamp when the todo_item was created",
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime,
            server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
        ),
        description="The timestamp when the todo_item was last updated",
    )

    # Foreign key association with the Project table
    project_id: int = Field(foreign_key="project.id")
