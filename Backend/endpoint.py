import json
from http import HTTPStatus

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import Response

from api import calling

router = APIRouter()

class EventSchema(BaseModel):
    """event schema - change accordingly"""
    prompt: str


@router.post("/", dependencies=[])
def handle_event(
    data: EventSchema,
) -> Response:
    # print(data)
    output = calling(data.prompt)

    return Response(
        content = json.dumps({"message": output}),
        status_code=HTTPStatus.ACCEPTED,
    )


