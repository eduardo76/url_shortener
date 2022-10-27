from typing import Dict
from abc import ABC, abstractmethod

from .url_domain import UrlDomain


class FindUrlInterface(ABC):
    """
    Find URL Interface
    """

    @abstractmethod
    def handle(self, url: str) -> Dict[bool, UrlDomain]:
        """
        Find URL
        """
        
        raise Exception("Method not implemented")
