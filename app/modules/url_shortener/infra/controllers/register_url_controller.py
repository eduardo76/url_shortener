from typing import Type

from ...domain.models.register_url_interface import RegisterUrlInterface
from .....shared.interface.router import RouterInterface
from .....shared.helpers import HttpRequest, HttpResponse
from .....shared.errors import HttpErrors


class RegisterUrlController(RouterInterface):
    """Register URL Controller"""

    def __init__(self, register_url_service: Type[RegisterUrlInterface]):
        """
        Constructor
        :param register_url_use_case: Type[RegisterUrlInterface]
        """
        self.register_url_service = register_url_service

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """
        Route
        :param http_request: Type[HttpRequest]
        :return: HttpResponse
        """

        response  = None

        if http_request.body:
            body = http_request.body

            if 'url' in body:
                url = body['url']

                response = self.register_url_service.register(url)
            else:
                response = {"success": False, "data": None} 

            if response['success'] is False:
                https_error = HttpErrors.error_422()
                return HttpResponse(status_code=https_error["status_code"], body=https_error["body"])

            return HttpResponse(status_code=201, body=response['data'])

        https_error = HttpErrors.error_400()
        return HttpResponse(status_code=https_error["status_code"], body=https_error["body"])



