from fastapi import FastAPI

from trabalho_final_prog_web.routes import todo_item

from ..routes import project, root


def mount_routes(app: FastAPI):
    app.include_router(root.router)
    app.include_router(project.router)
    app.include_router(todo_item.router)
    return app
