from werkzeug import Response
from werkzeug.exceptions import HTTPException


class RestError(HTTPException):
    def __init__(self, code: int, description: str | None = None, response: Response | None = None) -> None:
        super().__init__(description, response)
        self.code = code