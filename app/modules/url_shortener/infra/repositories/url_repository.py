import sys
from typing import List
from sqlalchemy.orm.exc import NoResultFound

from app.infra.config.db_base import DBConnectionHandler

from app.modules.url_shortener.infra.entities import UrlShortenerEntity
from app.modules.url_shortener.domain.repositories.url_repository_interface import UrlRepositoryInterface
from app.modules.url_shortener.domain.models.url_domain import UrlDomain


class UrlRepository(UrlRepositoryInterface):
    """
    Url repository
    """

    @classmethod
    def create(cls, data: UrlDomain) -> UrlDomain:
        """
        Create a new url

        :param url: UrlDomain
        :return: UrlDomain
        """

        with DBConnectionHandler() as db_connection:
            try:
                url_entity = UrlShortenerEntity(
                    long_url=data["long_url"],
                    short_url=data["short_url"],
                    id_hash=data["id_hash"],
                    hash_url=data["hash_url"],
                    status_url=data["status_url"],
                    total_access=data["total_access"],
                )

                db_connection.session.add(url_entity)
                db_connection.session.commit()

                return {
                    "success": True,
                    "message": "Url created successfully",
                    "data": {
                        "id_url": url_entity.id_url,
                        "long_url": url_entity.long_url,
                        "short_url": url_entity.short_url,
                        "id_hash": url_entity.id_hash,
                        "hash_url": url_entity.hash_url,
                        "status_url": url_entity.status_url,
                        "total_access": url_entity.total_access,
                        "created_at": url_entity.created_at,
                        "updated_at": url_entity.updated_at,
                    },
                }
            except Exception as e:
                db_connection.session.rollback()
            finally:
                db_connection.session.close()

    @classmethod
    def get_by_id(cls, url_id: int) -> UrlDomain:
        """
        Get url by id

        :param url_id: int
        :return: UrlDomain
        """

        with DBConnectionHandler() as db_connection:
            try:
                url_entity = db_connection.session.query(UrlShortenerEntity).filter_by(id_url=url_id).one()

                return {
                    "success": True,
                    "message": "Url found successfully",
                    "data": {
                        "id_url": url_entity.id_url,
                        "long_url": url_entity.long_url,
                        "short_url": url_entity.short_url,
                        "id_hash": url_entity.id_hash,
                        "hash_url": url_entity.hash_url,
                        "status_url": url_entity.status_url,
                        "total_access": url_entity.total_access,
                        "created_at": url_entity.created_at,
                        "updated_at": url_entity.updated_at,
                    }
                }
            except NoResultFound:
                return {"success": False, "data": "Url not found"}
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def get_by_hash(cls, hash_url: str) -> UrlDomain:
        """
        Get url by hash

        :param hash_url: str
        :return: UrlDomain
        """

        with DBConnectionHandler() as db_connection:
            try:
                url_entity = db_connection.session.query(UrlShortenerEntity).filter_by(hash_url=hash_url).one()

                return {
                    "success": True,
                    "message": "Hash already exists",
                    "data": {
                        "id_url": url_entity.id_url,
                        "long_url": url_entity.long_url,
                        "short_url": url_entity.short_url,
                        "id_hash": url_entity.id_hash,
                        "hash_url": url_entity.hash_url,
                        "status_url": url_entity.status_url,
                        "total_access": url_entity.total_access,
                        "created_at": url_entity.created_at,
                        "updated_at": url_entity.updated_at,
                    },
                }
            except NoResultFound:
                return {"success": False, "data": "hash not found"}
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def get_by_id_hash(cls, id_hash: int) -> UrlDomain:
        """
        Get url by id hash

        :param id_hash: int
        :return: UrlDomain
        """

        with DBConnectionHandler() as db_connection:
            try:
                url_entity = db_connection.session.query(UrlShortenerEntity).filter_by(id_hash=id_hash).one()

                return {
                    "success": True,
                    "message": "Hash found",
                    "data": {
                        "id_url": url_entity.id_url,
                        "long_url": url_entity.long_url,
                        "short_url": url_entity.short_url,
                        "id_hash": url_entity.id_hash,
                        "hash_url": url_entity.hash_url,
                        "status_url": url_entity.status_url,
                        "total_access": url_entity.total_access,
                        "created_at": url_entity.created_at,
                        "updated_at": url_entity.updated_at,
                    },
                }
            except NoResultFound:
                return {"success": False, "data": "hash not found"}
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def get_by_long_url(cls, long_url: str) -> UrlDomain:
        """
        Get url by long url

        :param long_url: str
        :return: UrlDomain
        """

        with DBConnectionHandler() as db_connection:
            try:
                url_entity = db_connection.session.query(UrlShortenerEntity).filter_by(long_url=long_url).one()

                return {
                    "success": True,
                    "message": "Url already exists",
                    "data": {
                        "id_url": url_entity.id_url,
                        "long_url": url_entity.long_url,
                        "short_url": url_entity.short_url,
                        "id_hash": url_entity.id_hash,
                        "hash_url": url_entity.hash_url,
                        "status_url": url_entity.status_url,
                        "total_access": url_entity.total_access,
                        "created_at": url_entity.created_at,
                        "updated_at": url_entity.updated_at,
                    },
                }
            except NoResultFound:
                return {"success": False, "data": "Url not found"}
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def get_all(cls) -> List[UrlDomain]:
        """
        Get all urls

        :return: List[UrlDomain]
        """

        with DBConnectionHandler() as db_connection:
            try:
                url_entities = db_connection.session.query(UrlShortenerEntity).all()

                return [url_entity.to_domain() for url_entity in url_entities]
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def update(cls, data: UrlDomain) -> UrlDomain:
        """
        Update url

        :param url: UrlDomain
        :return: UrlDomain
        """

        with DBConnectionHandler() as db_connection:
            try:
                url_entity = db_connection.session.query(UrlShortenerEntity).filter_by(id_url=data["id_url"]).one()

                url_entity.long_url = data["long_url"]
                url_entity.short_url = data["short_url"]
                url_entity.hash_url = data["hash_url"]
                url_entity.status_url = data["status_url"]
                url_entity.total_access = data["total_access"]

                db_connection.session.commit()

                return {
                    "success": True,
                    "message": "Url updated successfully",
                    "data": {
                        "id_url": url_entity.id_url,
                        "long_url": url_entity.long_url,
                        "short_url": url_entity.short_url,
                        "id_hash": url_entity.id_hash,
                        "hash_url": url_entity.hash_url,
                        "status_url": url_entity.status_url,
                        "total_access": url_entity.total_access,
                        "created_at": url_entity.created_at,
                        "updated_at": url_entity.updated_at,
                    },
                }
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def delete(cls, url_id: int) -> None:
        """
        Delete url

        :param url_id: int
        :return: None
        """

        with DBConnectionHandler() as db_connection:
            try:
                url_entity = db_connection.session.query(UrlShortenerEntity).filter_by(id_url=url_id).one()

                db_connection.session.delete(url_entity)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
