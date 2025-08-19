"""
User database. Operations: create, read, update, delete
"""

from html import escape
import logging
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from app.services.databases import session, User


class UsersData:
    """
    User database
    """

    def __init__(self):
        self.db = session

    def create(self, username: str, name: str = "") -> bool:
        """
        Create a new user
        :param username:
        :param name:
        :return:
        """
        try:
            username = escape(username)
            name = escape(name)
            user = User(name=name, username=username)
            self.db.add(user)
            self.db.commit()
            return True
        except IntegrityError as e:
            logging.error("User create fail: %s", e)
            self.db.rollback()
            return False

    def get_one(self, user_id: int) -> dict | None:
        """
        Get a single user by ID
        :param user_id:
        :return: User or None
        """
        try:
            query = select(User).where(User.id == user_id)
            result = self.db.execute(query)
            row = result.scalar_one_or_none()
            return {
                "id": row.id,
                "username": row.username,
                "name": row.name,
                "created_at": row.created_at.strftime("Y-m-d")
            }
        except ValueError as e:
            logging.error("User get_one fail: %s", e)
            return None

    def get_all(self) -> list | None:
        """
        Get all users
        :return: User or None
        """
        try:
            query = select(User)
            result = self.db.execute(query)
            rows = result.scalars().all()
            result = [
                {
                    "id": row.id,
                    "username": row.username,
                    "name": row.name,
                    "created_at": row.created_at.strftime("Y-m-d")
                }
                for row in rows]

            return result
        except ValueError as e:
            logging.error("Users get_all fail: %s", e)
            return None

    def update(self, user_id: int, username: str, name: str = "") -> bool:
        """
        Update a user
        :param user_id:
        :param username:
        :param name:
        :return:
        """
        try:
            query = select(User).where(User.id == user_id)
            result = self.db.execute(query)
            user = result.scalar_one_or_none()
            if user is None:
                return False
            user.name = escape(name)
            user.username = escape(username)
            self.db.commit()
            return True
        except IntegrityError as e:
            logging.error("User update fail: %s", e)
            self.db.rollback()
            return False

    def delete(self, user_id: int) -> bool:
        """
        Delete a user by ID
        :param user_id:
        :return: Bool
        """
        try:
            query = select(User).where(User.id == user_id)
            result = self.db.execute(query)
            row = result.scalar_one_or_none()
            if row is None:
                return False
            self.db.delete(row)
            self.db.commit()
            return True
        except ValueError as e:
            logging.error("User delete fail: %s", e)
            return False
