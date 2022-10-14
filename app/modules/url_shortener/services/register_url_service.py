from typing import Type, Dict

from app.modules.url_shortener.domain.repositories import UrlRepositoryInterface
from app.modules.url_shortener.domain.models import RegisterUrlInterface
from app.modules.url_shortener.domain.models import UrlDomain


class RegisterUrlService(RegisterUrlInterface):
    """
    Register URL Service
    """

    def __init__(self, url_repository: Type[UrlRepositoryInterface]):
        self.url_repository = url_repository

    
    def register(self, data: UrlDomain) -> Dict[bool, UrlDomain]:
        """
        Register URL
        """

        try:
            url_long = self.url_repository.get_by_long_url(data.long_url)

            if url_long:
                return {'success': False, 'data': url_long}
    
            hash_url = self.url_repository.get_by_hash(data.hash_url)

            if hash_url:
                return {'success': False, 'data': hash_url}

            url = self.url_repository.create(data)

            return {'success': True, 'data': url}
        except:
            raise Exception('Error to register URL')


