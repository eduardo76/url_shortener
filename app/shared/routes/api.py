
from fastapi import APIRouter, Request, Header, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel

from ..composer import register_url_composer, redirect_url_composer, find_url_composer
from ..adapter import fast_api_adapter

api = APIRouter()
templates = Jinja2Templates(directory="app/shared/static/templates")

@api.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("pages/home.html", {"request": request})


@api.get("/shortened/{id_url}", response_class=HTMLResponse)
async def shortened_url(request: Request, id_url: str):
    
    requestDict = dict()
    requestDict['request'] = request
    requestDict['body'] = id_url
    requestDict['header'] = Header

    response_data = fast_api_adapter(request=requestDict, router=find_url_composer())
    data = response_data.body['data']

    return templates.TemplateResponse("pages/shortened.html", {"request": request, "data": data})


class Url(BaseModel):
    long_url: str

@api.post("/shorten")
async def register_url(url: Url):
    """
    Register URL
    """

    message = {}
    request = dict()
    request['request'] = Request
    request['body'] = url.long_url
    request['header'] = Header

    response = fast_api_adapter(request=request, router=register_url_composer())

    if response.status_code < 300:
        message = {"success": True, "data": response.body}

        return message

    message = {"success": False, "data": response.body}

    return message


@api.get("/{hash}")
async def redirect_url(hash: str, response: Response):
    """
    Redirect URL
    """

    message = {}
    request = dict()
    request['request'] = Request
    request['body'] = hash
    request['header'] = Header

    response_adapter = fast_api_adapter(request=request, router=redirect_url_composer())

    if response_adapter.status_code < 300:
        message = {"success": True, "data": response_adapter.body}

        response.status_code = 302
        response.headers["Location"] = message['data']['data']['long_url']

        return response

    message = {"success": False, "data": response_adapter.body}

    return message