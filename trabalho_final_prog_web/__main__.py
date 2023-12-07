from fastapi import FastAPI

from .core.exception_handler import mount_custom_exceptions
from .core.log_filter import filter_log
from .core.routes import mount_routes
from .database import create_db_and_tables

app = FastAPI(
    title="TODO List API - Trabalho Final de Programação Web",
    summary="API para gerenciamento de tarefas.",
    version="1.0.0",
    contact={
        "name": "ph-cardoso",
        "url": "https://github.com/ph-cardoso/trabalho_final_prog_web",
    },
)


create_db_and_tables()
mount_routes(app)
mount_custom_exceptions(app)
filter_log()
