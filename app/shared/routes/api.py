
from fastapi import APIRouter, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel

from ..composer import register_url_composer, redirect_url_composer
from ..adapter import fast_api_adapter

api = APIRouter()
templates = Jinja2Templates(directory="app/shared/assets/templates")

@api.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("pages/home.html", {"request": request})


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


@api.get("/{hash}")
async def redirect_url(hash: str):
    """
    Redirect URL
    """

    message = {}
    request = dict()
    request['request'] = Request
    request['body'] = hash
    request['header'] = Header

    response = fast_api_adapter(request=request, router=redirect_url_composer())

    if response.status_code < 300:
        message = {"success": True, "data": response.body}

        return message

    message = {"success": False, "data": response.body}

    return message