from ..interface import RouterInterface
from ...modules.url_shortener.infra.controllers import FindUrlController
from ...modules.url_shortener.services import FindUrlService
from ...modules.url_shortener.infra.repositories import UrlRepository


def find_url_composer() -> RouterInterface:
    """
    Find URL Composer
    """
    url_repository = UrlRepository()
    find_url_service = FindUrlService(url_repository)
    find_url_controller = FindUrlController(find_url_service)

    return find_url_controller