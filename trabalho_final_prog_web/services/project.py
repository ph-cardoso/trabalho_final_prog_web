from sqlmodel import Session, select

from ..database import engine
from ..exceptions import ProjectNotFoundException, ServerErrorException
from ..models.db_models import Project
from ..models.project import ProjectCreationBody, ProjectStatus, ProjectUpdateBody


async def get_all_projects() -> list[Project]:
    with Session(engine) as session:
        db_projects = session.exec(select(Project)).all()
        return db_projects


async def get_project_by_id(project_id: int) -> Project:
    with Session(engine) as session:
        db_project = session.exec(
            select(Project).where(Project.id == project_id)
        ).first()

        if not db_project:
            raise ProjectNotFoundException(project_id)

        return db_project


async def create_project(req_body: ProjectCreationBody) -> Project:
    project = Project(**req_body.dict(), status=ProjectStatus.pending)
    with Session(engine) as session:
        try:
            session.add(project)
            session.commit()
            session.refresh(project)
        except Exception as e:
            session.rollback()
            raise ServerErrorException(original_exception=e) from e
    return project


async def update_project(project_id: int, req_body: ProjectUpdateBody) -> Project:
    with Session(engine) as session:
        db_project = session.exec(
            select(Project).where(Project.id == project_id)
        ).first()
        if db_project:
            for key, value in req_body.dict().items():
                setattr(db_project, key, value)
            session.commit()
            session.refresh(db_project)
        else:
            session.rollback()
            raise ProjectNotFoundException(project_id)
        return db_project


async def remove_project(project_id: int) -> Project:
    with Session(engine) as session:
        db_project = session.exec(
            select(Project).where(Project.id == project_id)
        ).first()
        if db_project:
            session.delete(db_project)
            session.commit()
        else:
            session.rollback()
            raise ProjectNotFoundException(project_id)
        return db_project
