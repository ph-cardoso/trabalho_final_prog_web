from fastapi import APIRouter, Form, Request
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from pathlib import Path

from ..models.todo_item import TodoItemCreationBody
from ..services.todo_item import create_todo_item, get_todo_item

from ..models.project import ProjectCreationBody
from ..services.project import create_project, get_all_projects

# Assuming that you are in the 'router' directory
template_path = Path(__file__).resolve().parent.parent / "templates"

# Get the absolute path
absolute_template_path = template_path.resolve()

router = APIRouter(tags=["/"])

templates = Jinja2Templates(directory=absolute_template_path)


class HealthCheckRes(BaseModel):
    status: str


@router.get("/healthz", summary="Health Check")
async def get_health_check() -> HealthCheckRes:
    return JSONResponse(content={"status": "ok"}, status_code=200)


# Rota para renderizar a página home
@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def render_home(request: Request):
    projects = await get_all_projects()
    todo_items = await get_todo_item()
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "title": "TODO List API",
            "header": "Bem vindo a API TODO List",
            "description": "Esta é uma API para gerenciar projetos e suas tarefas.",
            "footer": "Copyrigth © 2023 - Todos os direitos reservados.",
            "projects": projects,
            "todo_items": todo_items,
        },
    )


# Rota para renderizar a página create_project
@router.get("/create_project", response_class=HTMLResponse, include_in_schema=False)
async def render_create_project(request: Request):
    return templates.TemplateResponse(
        "create_project.html",
        {"request": request},
    )


# Rota para lidar com o envio do formulário de criação de projeto
@router.post("/create_project", response_class=RedirectResponse)
async def post_create_project(
    request: Request, name: str = Form(...), description: str = Form(...)
):
    # Crie um objeto ProjectCreationBody com os dados do formulário
    body = ProjectCreationBody(name=name, description=description)

    # Chame o serviço para criar o projeto
    await create_project(body)

    # Redirecione de volta à página inicial
    return RedirectResponse(url="/", status_code=303)


# Rota para renderizar a página create_todo_item
@router.get("/create_todo_item", response_class=HTMLResponse, include_in_schema=False)
async def render_create_todo_item(request: Request):
    return templates.TemplateResponse(
        "create_todo_item.html",
        {"request": request},
    )


# Rota para lidar com o envio do formulário de criação de projeto
@router.post("/create_todo_item", response_class=RedirectResponse)
async def post_create_todo_item(
    request: Request,
    project_id: str = Form(...),
    name: str = Form(...),
    description: str = Form(...),
    due_date: str = Form(...),
):
    # Crie um objeto ProjectCreationBody com os dados do formulário
    body = TodoItemCreationBody(
        project_id=project_id, name=name, description=description, due_date=due_date
    )

    # Chame o serviço para criar o projeto
    await create_todo_item(body)

    # Redirecione de volta à página inicial
    return RedirectResponse(url="/", status_code=303)
