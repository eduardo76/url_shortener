from typing import Type
from sqlalchemy.exc import IntegrityError


from ..interface import RouterInterface
from ..helpers import HttpRequest, HttpResponse
from ..errors import HttpErrors


def fast_api_adapter(request: any, router: Type[RouterInterface]) -> any:
    """
    Fast API Adapter
    :param request: any
    :param router: Type[RouterInterface]
    :return: any
    """


    query_params = request['request'].query_params
    http_request = HttpRequest(header=request['header'], body=request['body'], query=query_params)

    try:
        response = router.route(http_request)
    except IntegrityError as e:
        http_error = HttpErrors.error_409()
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])
    except Exception as exc:
        print(exc)
        http_error = HttpErrors.error_500()
        return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

    return response