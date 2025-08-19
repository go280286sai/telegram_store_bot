"""
Order status database
Operations: create, read, update, delete
"""
import logging
from html import escape
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.services.databases import session, OrderStatus


class OrderStatusData:
    """
    Order status database
    """

    def __init__(self):
        self.db = session

    def create(self, status: str) -> bool:
        """
        Create a new user
        :param status:
        :return:
        """
        try:
            order_status = OrderStatus(status=escape(status))
            self.db.add(order_status)
            self.db.commit()
            return True
        except IntegrityError as e:
            logging.error("OrderStatus create fail: %s", e)
            self.db.rollback()
            return False

    def get_one(self, order_status_id: int) -> dict | None:
        """
        Get a single user by ID
        :param order_status_id:
        :return: Dict or None
        """
        try:
            query = (select(OrderStatus)
                     .where(OrderStatus.id == order_status_id))
            result = self.db.execute(query)
            row = result.scalar_one_or_none()
            return {
                "id": row.id,
                "status": row.status,
                "created_at": row.created_at.strftime("Y-m-d")
            }
        except ValueError as e:
            logging.error("OrderStatus get_one fail: %s", e)
            return None

    def get_all(self) -> list | None:
        """
        Get all OrdersStatuses
        :return: List or None
        """
        try:
            query = select(OrderStatus)
            result = self.db.execute(query)
            rows = result.scalars().all()
            result = [
                {
                    "id": row.id,
                    "status": row.status,
                    "created_at": row.created_at.strftime("Y-m-d")
                }
                for row in rows]
            return result
        except ValueError as e:
            logging.error("OrderStatus get_all fail: %s", e)
            return None

    def update(self, order_status_id: int, status: str) -> bool:
        """
        Update a order status
        :param status:
        :param order_status_id:
        :return:
        """
        try:
            query = (select(OrderStatus)
                     .where(OrderStatus.id == order_status_id))
            result = self.db.execute(query)
            row = result.scalar_one_or_none()
            if row is None:
                return False
            row.status = escape(status)
            self.db.commit()
            return True
        except IntegrityError as e:
            logging.error("OrderStatus update fail: %s", e)
            self.db.rollback()
            return False

    def delete(self, order_status_id: int) -> bool:
        """
        Delete an order status by ID
        :param order_status_id:
        :return: Bool
        """
        try:
            query = (select(OrderStatus)
                     .where(OrderStatus.id == order_status_id))
            result = self.db.execute(query)
            row = result.scalar_one_or_none()
            if row is None:
                return False
            self.db.delete(row)
            self.db.commit()
            return True
        except ValueError as e:
            logging.error("OrderStatus delete fail: %s", e)
            return False
