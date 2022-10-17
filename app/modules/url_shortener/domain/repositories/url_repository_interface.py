from typing import List
from abc import ABC, abstractmethod

from ..models import UrlDomain

class UrlRepositoryInterface(ABC):
    """
    Url repository interface
    """

    @abstractmethod
    def create(self, url: UrlDomain) -> UrlDomain:
        """
        Create a new url
        """
        raise Exception("Method not implemented")

    @abstractmethod
    def get_by_id(self, url_id: int) -> UrlDomain:
        """
        Get url by id
        """
        raise Exception("Method not implemented")

    @abstractmethod
    def get_by_hash(self, hash_url: str) -> UrlDomain:
        """
        Get url by hash
        """
        raise Exception("Method not implemented")

    @abstractmethod
    def get_by_id_hash(self, id_hash: int) -> UrlDomain:
        """
        Get url by id hash
        """
        raise Exception("Method not implemented")

    @abstractmethod
    def get_by_long_url(self, long_url: str) -> UrlDomain:
        """
        Get url by long url
        """
        raise Exception("Method not implemented")

    @abstractmethod
    def get_all(self) -> List[UrlDomain]:
        """
        Get all urls
        """
        raise Exception("Method not implemented")

    @abstractmethod
    def update(self, url: UrlDomain) -> UrlDomain:
        """
        Update url
        """
        raise Exception("Method not implemented")

    @abstractmethod
    def delete(self, url: UrlDomain) -> UrlDomain:
        """
        Delete url
        """
        raise Exception("Method not implemented")