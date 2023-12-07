from fastapi import APIRouter

from ..models.db_models import Project
from ..models.project import ProjectCreationBody, ProjectUpdateBody
from ..services.project import (
    create_project,
    get_all_projects,
    get_project_by_id,
    remove_project,
    update_project,
)

router = APIRouter(tags=["project"], prefix="/project")


@router.get("/", summary="Lista todos os projetos", status_code=200)
async def get_list_all_projects() -> list[Project]:
    return await get_all_projects()


@router.get("/{project_id}", summary="Lista um projeto por id", status_code=200)
async def get_list_project_by_id(project_id: int) -> Project:
    return await get_project_by_id(project_id)


@router.post("/", summary="Cria um novo projeto", status_code=201)
async def post_create_new_list(
    body_paylod: ProjectCreationBody,
) -> Project:
    return await create_project(body_paylod)


@router.put("/{project_id}", summary="Atualiza um projeto", status_code=200)
async def put_update_project(
    project_id: int, body_paylod: ProjectUpdateBody
) -> Project:
    return await update_project(project_id, body_paylod)


@router.delete("/{project_id}", summary="Deleta um projeto", status_code=200)
async def delete_project(project_id: int) -> Project:
    return await remove_project(project_id)
