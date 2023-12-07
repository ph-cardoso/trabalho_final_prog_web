from venv import logger

from decouple import config
from sqlmodel import SQLModel, create_engine

# Retrieve database information from environment variables
mysql_user = config("DB_USER", cast=str, default="prog_web_user")
mysql_password = config("DB_PASSWORD", cast=str, default="prog_web_token")
mysql_host = config("DB_HOST", cast=str, default="localhost")
mysql_port = config("DB_PORT", cast=int, default=3306)
mysql_database = config("DB_NAME", cast=str, default="todo_db")

# MySQL configuration
mysql_url = f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}"

engine = create_engine(mysql_url)


def create_db_and_tables():
    from .models.db_models import Project

    logger.info("Creating database and tables")
    logger.info(Project)
    SQLModel.metadata.create_all(engine)
