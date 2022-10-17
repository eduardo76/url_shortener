from ..interface import RouterInterface
from ...modules.url_shortener.infra.controllers import RedirectUrlController
from ...modules.url_shortener.services import RedirectUrlService
from ...modules.url_shortener.infra.repositories import UrlRepository


def redirect_url_composer() -> RouterInterface:
    """
    Register URL Composer
    """
    url_repository = UrlRepository()
    redirect_url_service = RedirectUrlService(url_repository)
    redirect_url_controller = RedirectUrlController(redirect_url_service)

    return redirect_url_controller

