"""
Product database
Operations: create, read, update, delete
"""
import logging
from html import escape
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.services.databases import session, Product


class ProductData:
    """
    Product database
    """

    def __init__(self):
        self.db = session

    def create(self, **kwargs) -> bool:
        """
        Create a new product database
        :return:
        """
        try:
            name = kwargs.get('name', "")
            description = kwargs.get('description', "")
            price = kwargs.get('price', 0)
            is_service = kwargs.get('is_service', 0)
            amount = kwargs.get('amount', 0)
            query = Product(
                name=escape(name),
                description=escape(description),
                price=price,
                is_service=is_service,
                amount=amount
            )
            self.db.add(query)
            self.db.commit()
            return True
        except IntegrityError as e:
            logging.error("Product create fail: %s", e)
            self.db.rollback()
            return False

    def get_one(self, product_id: int) -> dict | None:
        """
        Get a single product by ID
        :param product_id:
        :return: Dict or None
        """
        try:
            query = select(Product).where(Product.id == product_id)
            result = self.db.execute(query)
            row = result.scalar_one_or_none()
            return {
                "id": row.id,
                "name": row.name,
                "description": row.description,
                "price": row.price,
                "is_service": row.is_service,
                "amount": row.amount,
                "created_at": row.created_at.strftime("Y-m-d")
            }
        except ValueError as e:
            logging.error("Product get_one fail: %s", e)
            return None

    def get_all(self) -> list | None:
        """
        Get all products
        :return: List or None
        """
        try:
            query = select(Product)
            result = self.db.execute(query)
            rows = result.scalars().all()
            result = [
                {
                    "id": row.id,
                    "name": row.name,
                    "description": row.description,
                    "price": row.price,
                    "is_service": row.is_service,
                    "amount": row.amount,
                    "created_at": row.created_at.strftime("Y-m-d")
                }
                for row in rows]
            return result
        except ValueError as e:
            logging.error("Products get_all fail: %s", e)
            return None

    def update(self, product_id: int, **kwargs) -> bool:
        """
        Update Product database
        :param product_id:
        :return:
        """
        try:
            name = kwargs.get('name', "")
            description = kwargs.get('description', "")
            price = kwargs.get('price', 0)
            is_service = kwargs.get('is_service', 0)
            amount = kwargs.get('amount', 0)
            query = select(Product).where(Product.id == product_id)
            result = self.db.execute(query)
            row = result.scalar_one_or_none()
            if row is None:
                return False
            row.name = escape(name)
            row.description = escape(description)
            row.price = float(price)
            row.is_service = is_service
            row.amount = amount
            self.db.commit()
            return True
        except IntegrityError as e:
            logging.error("Product update fail: %s", e)
            self.db.rollback()
            return False

    def delete(self, product_id: int) -> bool:
        """
        Delete product by ID
        :param product_id:
        :return: Bool
        """
        try:
            query = select(Product).where(Product.id == product_id)
            result = self.db.execute(query)
            row = result.scalar_one_or_none()
            if row is None:
                return False
            self.db.delete(row)
            self.db.commit()
            return True
        except ValueError as e:
            logging.error("Product delete fail: %s", e)
            return False
