
from fastapi import APIRouter, Request, Header
from pydantic import BaseModel

from ..composer import register_url_composer
from ..adapter import fast_api_adapter

api = APIRouter()


@api.post("/shorten")
async def register_url(url: str):
    """
    Register URL
    """

    message = {}
    request = dict()
    request['request'] = Request
    request['body'] = url
    request['header'] = Header

    response = fast_api_adapter(request=request, router=register_url_composer())


    if response.status_code < 300:
        message = {"success": True, "data": response.body}

        return message

    message = {"success": False, "data": response.body}



