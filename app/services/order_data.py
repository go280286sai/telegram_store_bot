"""
Order database
Operations: create, read, update, delete
"""
import logging
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.services.databases import (session, Order,
                                    Delivery, OrderStatus, Product, User)


class OrderData:
    """
    Order database
    """

    def __init__(self):
        self.db = session

    def create(self,
               user_id: int,
               product_id: int,
               delivery_id: int,
               status_id: int
               ) -> bool:
        """
        Create a new delivery
        :param status_id:
        :param delivery_id:
        :param product_id:
        :param user_id:
        :return:
        """
        try:
            query = Order(
                user_id=int(user_id),
                product_id=int(product_id),
                delivery_id=int(delivery_id),
                status_id=int(status_id)
            )
            self.db.add(query)
            self.db.commit()
            return True
        except IntegrityError as e:
            logging.error("Order create fail: %s", e)
            self.db.rollback()
            return False

    def get_one(self, order_id: int) -> list | None:
        """
        Get a single delivery by ID
        :param order_id:
        :return: List or None
        """
        try:
            query = (select(
                Order.id.label('id'),
                Order.delivery_id.label('delivery_id'),
                Order.status_id.label('status_id'),
                Order.product_id.label('product_id'),
                Order.user_id.label('user_id'),
                Order.created_at.label('created_at'),
                Delivery.name.label("delivery_name"),
                OrderStatus.status.label("order_status_name"),
                Product.name.label("product_name"),
                User.username.label("username"))
                     .join(Delivery, Order.delivery_id == Delivery.id)
                     .join(OrderStatus, Order.status_id == OrderStatus.id)
                     .join(Product, Order.product_id == Product.id)
                     .join(User, Order.user_id == User.id)
                     .where(Order.id == order_id))
            result = self.db.execute(query)
            rows = result.all()
            return [{
                "id": row.id,
                "delivery_id": row.delivery_id,
                "order_status_id": row.status_id,
                "product_id": row.product_id,
                "user_id": row.user_id,
                "delivery_name": row.delivery_name,
                "order_status_name": row.order_status_name,
                "product_name": row.product_name,
                "username": row.username,
                "created_at": row.created_at.strftime("Y-m-d")
            } for row in rows]
        except ValueError as e:
            logging.error("Order get_one fail: %s", e)
            return None

    def get_all(self) -> list | None:
        """
        Get all orders
        :return: List or None
        """
        try:
            query = (select(
                Order.id.label('id'),
                Order.delivery_id.label('delivery_id'),
                Order.status_id.label('status_id'),
                Order.product_id.label('product_id'),
                Order.user_id.label('user_id'),
                Order.created_at.label('created_at'),
                Delivery.name.label("delivery_name"),
                OrderStatus.status.label("order_status_name"),
                Product.name.label("product_name"),
                User.username.label("username"))
                     .join(Delivery, Order.delivery_id == Delivery.id)
                     .join(OrderStatus, Order.status_id == OrderStatus.id)
                     .join(Product, Order.product_id == Product.id)
                     .join(User, Order.user_id == User.id))
            result = self.db.execute(query)
            rows = result.all()
            return [{
                "id": row.id,
                "delivery_id": row.delivery_id,
                "order_status_id": row.status_id,
                "product_id": row.product_id,
                "user_id": row.user_id,
                "delivery_name": row.delivery_name,
                "order_status_name": row.order_status_name,
                "product_name": row.product_name,
                "username": row.username,
                "created_at": row.created_at.strftime("Y-m-d")
            } for row in rows]
        except ValueError as e:
            logging.error("Orders get_all fail: %s", e)
            return None

    def get_all_user(self, user_id: int) -> list | None:
        """
        Get all orders
        :param user_id:
        :return: List or None
        """
        try:
            query = (select(
                Order.id.label('id'),
                Order.delivery_id.label('delivery_id'),
                Order.status_id.label('status_id'),
                Order.product_id.label('product_id'),
                Order.user_id.label('user_id'),
                Order.created_at.label('created_at'),
                Delivery.name.label("delivery_name"),
                OrderStatus.status.label("order_status_name"),
                Product.name.label("product_name"),
                User.username.label("username"))
                     .join(Delivery, Order.delivery_id == Delivery.id)
                     .join(OrderStatus, Order.status_id == OrderStatus.id)
                     .join(Product, Order.product_id == Product.id)
                     .join(User, Order.user_id == User.id)
                     .where(Order.user_id == user_id))
            result = self.db.execute(query)
            rows = result.all()
            return [{
                "id": row.id,
                "delivery_id": row.delivery_id,
                "order_status_id": row.status_id,
                "product_id": row.product_id,
                "user_id": row.user_id,
                "delivery_name": row.delivery_name,
                "order_status_name": row.order_status_name,
                "product_name": row.product_name,
                "username": row.username,
                "created_at": row.created_at.strftime("Y-m-d")
            } for row in rows]
        except ValueError as e:
            logging.error("Orders get_all fail: %s", e)
            return None

    def update(self, order_id: int, **kwargs) -> bool:
        """
        Update delivery
        :param status_id:
        :param product_id:
        :param user_id:
        :param order_id:
        :param delivery_id:
        :return:
        """
        try:
            user_id = kwargs.get("user_id", 0)
            product_id = kwargs.get("product_id", 0)
            delivery_id = kwargs.get("delivery_id", 0)
            status_id = kwargs.get("status_id", 0)
            query = select(Order).where(Order.id == order_id)
            result = self.db.execute(query)
            row = result.scalar_one_or_none()
            if row is None:
                return False
            row.user_id = user_id
            row.product_id = product_id
            row.delivery_id = delivery_id
            row.status_id = status_id
            self.db.commit()
            return True
        except IntegrityError as e:
            logging.error("Order update fail: %s", e)
            self.db.rollback()
            return False

    def delete(self, order_id: int) -> bool:
        """
        Delete order by ID
        :param order_id:
        :return: Bool
        """
        try:
            query = select(Order).where(Order.id == order_id)
            result = self.db.execute(query)
            row = result.scalar_one_or_none()
            if row is None:
                return False
            self.db.delete(row)
            self.db.commit()
            return True
        except ValueError as e:
            logging.error("Order delete fail: %s", e)
            return False
