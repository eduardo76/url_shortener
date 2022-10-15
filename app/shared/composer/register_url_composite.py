from ..interface import RouterInterface
from ...modules.url_shortener.infra.controllers import RegisterUrlController
from ...modules.url_shortener.services import RegisterUrlService
from ...modules.url_shortener.infra.repositories import UrlRepository


def register_url_composer() -> RouterInterface:
    """
    Register URL Composer
    """
    url_repository = UrlRepository()
    register_url_service = RegisterUrlService(url_repository)
    register_url_controller = RegisterUrlController(register_url_service)

    return register_url_controller