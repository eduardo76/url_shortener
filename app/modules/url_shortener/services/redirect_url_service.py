import sys

from typing import Type, Dict

from app.modules.url_shortener.domain.repositories import UrlRepositoryInterface
from app.modules.url_shortener.domain.models import RedirectUrlInterface
from app.modules.url_shortener.domain.models import UrlDomain
from app.shared.utils.utils import from_base62


class RedirectUrlService(RedirectUrlInterface):
    """
    Redirect URL Service
    """

    def __init__(self, url_repository: Type[UrlRepositoryInterface]):
        """
        Constructor

        :param url_repository: Type[UrlRepositoryInterface]
        """
        self.url_repository = url_repository

    def redirect(self, hash: str) -> Dict[bool, UrlDomain]:
        """
        Register URL

        :param data: UrlDomain
        :return: Dict[bool, UrlDomain]
        """

        try:

            response = None

            id_hash = from_base62(hash)

            response = self.url_repository.get_by_id_hash(id_hash)

            if response["success"] is True:
                data = {
                    "id_url": response["data"]["id_url"],
                    "long_url": response["data"]["long_url"],
                    "short_url": response["data"]["short_url"],
                    "id_hash": response["data"]["id_hash"],
                    "hash_url": response["data"]["hash_url"],
                    "status_url": response["data"]["status_url"],
                    "total_access": response["data"]["total_access"] + 1,
                }
                response = self.url_repository.update(data)
                return {"success": True, "data": response}

            return {"success": False, "data": None}

        except Exception as e:
            return {"success": False, "data": None}