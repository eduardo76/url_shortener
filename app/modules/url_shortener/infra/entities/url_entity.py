import enum
from sqlalchemy.sql import func
from sqlalchemy import Column, String, Integer, ForeignKey, Enum, DateTime
from app.modules.url_shortener.domain.models.url_domain import UrlDomain

from app.infra.config.db_base import Base


class Status(enum.Enum):
    active = "active"
    inactive = "inactive"


class UrlShortenerEntity(Base):
    __tablename__ = "url_shortener"

    id_url = Column(Integer, primary_key=True, index=True)
    long_url = Column(String, nullable=False, unique=True)
    hash_url = Column(String, nullable=False)
    status_url = Column(Enum(Status), nullable=False)
    total_access = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, id_url: int, long_url: str, hash_url: str, total_access: str, status_url: str, created_at: str, updated_at: str):
        self.id_url = id_url
        self.long_url = long_url
        self.hash_url = hash_url
        self.total_access = total_access
        self.status_url = status_url
        self.created_at = created_at
        self.updated_at = updated_at

    def to_domain(self) -> UrlDomain:
        return UrlDomain(
            id_url=self.id_url,
            long_url=self.long_url,
            hash_url=self.hash_url,
            total_access=self.total_access,
            status_url=self.status_url,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    def __repr__(self):
        return f"UrlEntity(id_url={self.id_url}, long_url={self.long_url}"

    def __eq__(self, other):
        if not isinstance(other, UrlShortenerEntity):
            return False
        return self.id_url == other.url_id

    def __hash__(self):
        return hash(self.id_url)