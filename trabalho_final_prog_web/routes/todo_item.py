from fastapi import APIRouter

from ..models.db_models import TodoItem
from ..models.todo_item import TodoItemCreationBody, TodoItemUpdateBody
from ..services.todo_item import (
    create_todo_item,
    get_todo_item,
    get_todo_item_by_id,
    list_todo_items_by_project_id,
    remove_todo_item,
    update_todo_item,
)

router = APIRouter(tags=["todo_item"], prefix="/todo_item")


@router.get("/", summary="Lista todos os itens de projeto")
async def get_list_todo_item() -> list[TodoItem]:
    return await get_todo_item()


@router.post("/", summary="Cria um novo item de projeto")
async def post_create_new_todo_item(body_paylod: TodoItemCreationBody) -> TodoItem:
    return await create_todo_item(body_paylod)


@router.get("/{todo_item_id}", summary="Lista um item de um projeto por id")
async def get_list_todo_item_by_id(todo_item_id: int) -> TodoItem:
    return await get_todo_item_by_id(todo_item_id)


@router.put("/{todo_item_id}", summary="Atualiza um item de projeto")
async def put_update_project(
    todo_item_id: int, body_paylod: TodoItemUpdateBody
) -> TodoItem:
    return await update_todo_item(todo_item_id, body_paylod)


@router.delete("/{todo_item_id}", summary="Deleta um item de projeto")
async def delete_todo_item(todo_item_id: int) -> TodoItem:
    return await remove_todo_item(todo_item_id)


@router.get("/{project_id}/items", summary="Lista todos os itens de um projeto")
async def get_list_all_todo_items(project_id: int) -> list[TodoItem]:
    return await list_todo_items_by_project_id(project_id)
