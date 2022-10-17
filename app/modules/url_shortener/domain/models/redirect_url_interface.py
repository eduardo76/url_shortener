from typing import Dict
from abc import ABC, abstractmethod

from .url_domain import UrlDomain


class RedirectUrlInterface(ABC):
    """
    Redirect URL Interface
    """

    @abstractmethod
    def redirect(self, url: str) -> Dict[bool, UrlDomain]:
        """
        Redirect URL
        """
        
        raise Exception("Method not implemented")
