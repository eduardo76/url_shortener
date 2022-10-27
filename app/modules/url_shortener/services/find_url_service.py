import sys

from typing import Type, Dict

from app.modules.url_shortener.domain.repositories import UrlRepositoryInterface
from app.modules.url_shortener.domain.models import FindUrlInterface
from app.modules.url_shortener.domain.models import UrlDomain


class FindUrlService(FindUrlInterface):
    """
    Find URL Service by id
    """

    def __init__(self, url_repository: Type[UrlRepositoryInterface]):
        """
        Constructor

        :param url_repository: Type[UrlRepositoryInterface]
        """
        self.url_repository = url_repository

    def handle(self, url_id: str) -> Dict[bool, UrlDomain]:
        """
        Find URL by id

        :param data: UrlDomain
        :return: Dict[bool, UrlDomain]
        """

        try:
            response = self.url_repository.get_by_id(url_id)

            if response["success"] is True:
                return {"success": True, "data": response}

            return {"success": False, "data": response}

        except Exception as e:
            print("===== Error 02 on line {} ======".format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

            raise Exception("Error to find URL by id")
