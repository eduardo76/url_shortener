import sys

from typing import Type, Dict

from app.modules.url_shortener.domain.repositories import UrlRepositoryInterface
from app.modules.url_shortener.domain.models import RegisterUrlInterface
from app.modules.url_shortener.domain.models import UrlDomain
from app.shared.utils.utils import to_base62, generate_id

class RegisterUrlService(RegisterUrlInterface):
    """
    Register URL Service
    """

    def __init__(self, url_repository: Type[UrlRepositoryInterface]):
        """
        Constructor

        :param url_repository: Type[UrlRepositoryInterface]
        """
        self.url_repository = url_repository

    
    def register(self, url: str) -> Dict[bool, UrlDomain]:
        """
        Register URL

        :param data: UrlDomain
        :return: Dict[bool, UrlDomain]
        """

        try:
            response = None

            id = generate_id()
            generated_hash = to_base62(id)
            
            data = {
                "long_url": url,
                "hash_url": generated_hash,
                "status_url": "active",
                "total_access": 0,
            }   


            response = self.url_repository.get_by_long_url(data['long_url'])

            if response['success'] is True:
                return {'success': True, 'data': response}
    
            # hash_url = self.url_repository.get_by_hash(data['hash_url'])

            # if hash_url['success'] is True:
            #     return {'success': False, 'data': hash_url}

            url = self.url_repository.create(data)


            return {'success': True, 'data': url}
        except Exception as e:
            print('===== Error 02 on line {} ======'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

            raise Exception('Error to register URL')


