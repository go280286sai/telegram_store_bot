"""
Delivery database
Operations: create, read, update, delete
"""
import logging
from html import escape
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.services.databases import session, Delivery


class DeliveryData:
    """
    Delivery status database
    """

    def __init__(self):
        self.db = session

    def create(self, name: str, description: str) -> bool:
        """
        Create a new delivery
        :param description:
        :param name:
        :return:
        """
        try:
            query = Delivery(
                name=escape(name),
                description=escape(description)
            )
            self.db.add(query)
            self.db.commit()
            return True
        except IntegrityError as e:
            logging.error("Delivery create fail: %s", e)
            self.db.rollback()
            return False

    def get_one(self, delivery_id: int) -> dict | None:
        """
        Get a single delivery by ID
        :param delivery_id:
        :return: Dict or None
        """
        try:
            query = select(Delivery).where(Delivery.id == delivery_id)
            result = self.db.execute(query)
            row = result.scalar_one_or_none()
            return {
                "id": row.id,
                "name": row.name,
                "description": row.description,
                "created_at": row.created_at.strftime("Y-m-d")
            }
        except ValueError as e:
            logging.error("Description get_one fail: %s", e)
            return None

    def get_all(self) -> list | None:
        """
        Get all deliveries
        :return: List or None
        """
        try:
            query = select(Delivery)
            result = self.db.execute(query)
            rows = result.scalars().all()
            result = [
                {
                    "id": row.id,
                    "name": row.name,
                    "description": row.description,
                    "created_at": row.created_at.strftime("Y-m-d")
                }
                for row in rows]
            return result
        except ValueError as e:
            logging.error("Deliveries get_all fail: %s", e)
            return None

    def update(self, delivery_id: int, name: str, description: str) -> bool:
        """
        Update delivery
        :param description:
        :param name:
        :param delivery_id:
        :return:
        """
        try:
            query = select(Delivery).where(Delivery.id == delivery_id)
            result = self.db.execute(query)
            row = result.scalar_one_or_none()
            if row is None:
                return False
            row.name = escape(name)
            row.description = escape(description)
            self.db.commit()
            return True
        except IntegrityError as e:
            logging.error("Delivery update fail: %s", e)
            self.db.rollback()
            return False

    def delete(self, delivery_id: int) -> bool:
        """
        Delete delivery by ID
        :param delivery_id:
        :return: Bool
        """
        try:
            query = select(Delivery).where(Delivery.id == delivery_id)
            result = self.db.execute(query)
            row = result.scalar_one_or_none()
            if row is None:
                return False
            self.db.delete(row)
            self.db.commit()
            return True
        except ValueError as e:
            logging.error("Delivery delete fail: %s", e)
            return False
