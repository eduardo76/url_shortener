from typing import Type

from ...domain.models import FindUrlInterface
from .....shared.interface.router import RouterInterface
from .....shared.helpers import HttpRequest, HttpResponse
from .....shared.errors import HttpErrors


class FindUrlController(RouterInterface):
    """FInd URL Controller"""

    def __init__(self, find_url_service: Type[FindUrlInterface]):
        """
        Constructor
        :param find_url_service: Type[FindUrlInterface]
        """
        self.find_url_service = find_url_service

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """
        Route
        :param http_request: Type[HttpRequest]
        :return: HttpResponse
        """

        response  = None

        if http_request.body:
            body = http_request.body

            if body:
                response = self.find_url_service.handle(body)
            else:
                response = {"success": False, "data": None} 

            if response['success'] is False:
                https_error = HttpErrors.error_404()
                return HttpResponse(status_code=https_error["status_code"], body=https_error["body"])

            return HttpResponse(status_code=201, body=response['data'])

        https_error = HttpErrors.error_400()
        return HttpResponse(status_code=https_error["status_code"], body=https_error["body"])



