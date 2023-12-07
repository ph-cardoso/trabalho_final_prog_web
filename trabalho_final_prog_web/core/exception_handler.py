from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from ..exceptions import (
    ProjectNotFoundException,
    ServerErrorException,
    TodoItemNotFoundException,
)


def mount_custom_exceptions(app: FastAPI):
    @app.exception_handler(ServerErrorException)
    async def server_error_exception_handler(
        request: Request, exc: ServerErrorException
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.detail,
        )

    @app.exception_handler(TodoItemNotFoundException)
    async def todo_item_not_found_exception_handler(
        request: Request, exc: TodoItemNotFoundException
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.detail,
        )

    @app.exception_handler(ProjectNotFoundException)
    async def project_not_found_exception_handler(
        request: Request, exc: ProjectNotFoundException
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.detail,
        )
