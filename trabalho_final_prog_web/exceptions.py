# Custom exception for project not found
from fastapi import HTTPException


# Custom exception for project not found
class ProjectNotFoundException(HTTPException):
    def __init__(self, project_id: int):
        super().__init__(
            status_code=404,
            detail={
                "error": "Project not found",
                "user_help": f"Project with ID {project_id} does not exist",
            },
        )


class TodoItemNotFoundException(HTTPException):
    def __init__(self, todo_item_id: int):
        super().__init__(
            status_code=404,
            detail={
                "error": "Todo Item not found",
                "user_help": f"Todo Item with ID {todo_item_id} does not exist",
            },
        )


# Custom exception for generic server errors
class ServerErrorException(HTTPException):
    def __init__(self, original_exception: Exception):
        super().__init__(
            status_code=500,
            detail={
                "error": "Internal Server Error",
                "user_help": "An unexpected error occurred on the server",
                "original_exception": str(original_exception),
            },
        )
