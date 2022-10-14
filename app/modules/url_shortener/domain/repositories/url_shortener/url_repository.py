from typing import List
from sqlalchemy.orm.exc import NoResultFound

from app.infra.config.db_base import DBConnectionHandler

from app.modules.url_shortener.infra.entities import UrlShortenerEntity
from app.modules.url_shortener.domain.models.url_shortener.url_repository_interface import UrlRepositoryInterface
from app.modules.url_shortener.domain.models.url_shortener.url_domain import UrlDomain


class UrlRepository(UrlRepositoryInterface):
    """
    Url repository
    """

    @classmethod
    def create(cls, url: UrlDomain) -> UrlDomain:
        """
        Create a new url

        :param url: UrlDomain
        :return: UrlDomain
        """

        try:
            with DBConnectionHandler() as db_connection:
                url_entity = UrlShortenerEntity(
                    id_url=url.id_url,
                    long_url=url.long_url,
                    hash_url=url.hash_url,
                    status_url=url.status_url
                )

                db_connection.session.add(url_entity)
                db_connection.session.commit()

                return url_entity.to_domain()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

    @classmethod
    def get_by_id(cls, url_id: int) -> UrlDomain:
        """
        Get url by id

        :param url_id: int
        :return: UrlDomain
        """

        try:
            with DBConnectionHandler() as db_connection:
                url_entity = db_connection.session.query(UrlShortenerEntity).filter_by(id_url=url_id).one()

                return url_entity.to_domain()
        except NoResultFound:
            return 'Url not found'
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

        try:
            with DBConnectionHandler() as db_connection:
                url_entity = db_connection.session.query(UrlShortenerEntity).filter_by(hash_url=hash_url).one()

                return url_entity.to_domain()
        except NoResultFound:
            return 'Url not found'
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

        try:
            with DBConnectionHandler() as db_connection:
                url_entity = db_connection.session.query(UrlShortenerEntity).filter_by(long_url=long_url).one()

                return url_entity.to_domain()
        except NoResultFound:
            return 'Url not found'
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

        try:
            with DBConnectionHandler() as db_connection:
                url_entities = db_connection.session.query(UrlShortenerEntity).all()

                return [url_entity.to_domain() for url_entity in url_entities]
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()

    @classmethod
    def update(cls, url: UrlDomain) -> UrlDomain:
        """
        Update url

        :param url: UrlDomain
        :return: UrlDomain
        """

        try:
            with DBConnectionHandler() as db_connection:
                url_entity = db_connection.session.query(UrlShortenerEntity).filter_by(id_url=url.id_url).one()

                url_entity.long_url = url.long_url
                url_entity.hash_url = url.hash_url
                url_entity.status_url = url.status_url

                db_connection.session.commit()

                return url_entity.to_domain()
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

        try:
            with DBConnectionHandler() as db_connection:
                url_entity = db_connection.session.query(UrlShortenerEntity).filter_by(id_url=url_id).one()

                db_connection.session.delete(url_entity)
                db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
