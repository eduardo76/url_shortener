import enum
from sqlalchemy.sql import func
from sqlalchemy import Column, String, Integer, ForeignKey, Enum, DateTime
from app.modules.url_shortener.domain.models.url_domain import UrlDomain

from app.infra.config.db_base import Base


class StatusEnum(enum.Enum):
    active = "active"
    inactive = "inactive"


class UrlShortenerEntity(Base):
    __tablename__ = "url_shortener"

    id_url = Column(Integer, primary_key=True, autoincrement=True, index=True)
    long_url = Column(String(255), unique=True)
    short_url = Column(String(255), unique=True)
    id_hash = Column(Integer, unique=True)
    hash_url = Column(String(255), unique=True)
    status_url = Column(Enum(StatusEnum))
    total_access = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now())


    def to_domain(self) -> UrlDomain:
        return UrlDomain(
            id_url=self.id_url,
            long_url=self.long_url,
            id_hash=self.id_hash,
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
        return self.id_url == other.id_url
