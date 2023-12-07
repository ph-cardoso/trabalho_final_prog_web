from datetime import datetime

from sqlmodel import Session, select

from ..database import engine
from ..exceptions import (
    ProjectNotFoundException,
    ServerErrorException,
    TodoItemNotFoundException,
)
from ..models.db_models import Project, TodoItem
from ..models.todo_item import TodoItemCreationBody, TodoItemStatus, TodoItemUpdateBody


async def get_todo_item() -> list[TodoItem]:
    with Session(engine) as session:
        todo_items = session.exec(select(TodoItem)).all()
        return todo_items


async def get_todo_item_by_id(todo_item_id: int) -> TodoItem:
    with Session(engine) as session:
        todo_item = session.exec(
            select(TodoItem).where(TodoItem.id == todo_item_id)
        ).first()

        if not todo_item:
            raise TodoItemNotFoundException(todo_item_id)

        return todo_item


async def create_todo_item(req_body: TodoItemCreationBody) -> TodoItem:
    with Session(engine) as session:
        try:
            todo_item = TodoItem(**req_body.dict(), status=TodoItemStatus.pending)
            session.add(todo_item)
            session.commit()
            session.refresh(todo_item)
        except Exception as e:
            session.rollback()
            raise ServerErrorException(original_exception=e) from e
        return todo_item


async def update_todo_item(todo_item_id: int, req_body: TodoItemUpdateBody) -> TodoItem:
    with Session(engine) as session:
        todo_item = session.exec(
            select(TodoItem).where(TodoItem.id == todo_item_id)
        ).first()
        if todo_item:
            for key, value in req_body.dict().items():
                setattr(todo_item, key, value)
            todo_item.updated_at = datetime.now()
            session.commit()
            session.refresh(todo_item)
        return todo_item


async def remove_todo_item(todo_item_id: int) -> TodoItem:
    with Session(engine) as session:
        todo_item = session.exec(
            select(TodoItem).where(TodoItem.id == todo_item_id)
        ).first()
        if todo_item:
            session.delete(todo_item)
            session.commit()
        return todo_item


async def list_todo_items_by_project_id(project_id: int) -> list[TodoItem]:
    with Session(engine) as session:
        project = session.exec(select(Project).where(Project.id == project_id)).first()
        if not project:
            raise ProjectNotFoundException(project_id)

        todo_items = session.exec(
            select(TodoItem).where(TodoItem.project_id == project_id)
        ).all()
        return todo_items
