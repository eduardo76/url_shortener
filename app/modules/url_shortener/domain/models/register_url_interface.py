from typing import Dict
from abc import ABC, abstractmethod

from .url_domain import UrlDomain


class RegisterUrlInterface(ABC):
    """
    Register URL Interface
    """

    @abstractmethod
    def register(self, url: str) -> Dict[bool, UrlDomain]:
        """
        Register URL
        """
        
        raise Exception("Method not implemented")
