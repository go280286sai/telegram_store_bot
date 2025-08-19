"""
Main data base struct
"""
# pylint disable=too-few-public-methods
# pylint disable=unnecessary-pass
from datetime import datetime
from sqlalchemy import (Column, Integer, String,
                        DateTime, ForeignKey, create_engine, Float)
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///database.db')


# pylint: disable=too-few-public-methods
class Base(DeclarativeBase):
    """
    Base class for all models.
    """
    pass


class User(Base):
    """
    User model.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    username = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Product(Base):
    """
    Product model.
    """
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, default=0)
    is_service = Column(Integer, default=0)
    amount = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)


class OrderStatus(Base):
    """
    Order status model.
    """
    __tablename__ = 'order_status'
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)


class Delivery(Base):
    """
    Delivery model.
    """
    __tablename__ = 'deliveries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Order(Base):
    """
    Order model.
    """
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        Integer,
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False
    )
    product_id = Column(
        Integer,
        ForeignKey('products.id', ondelete='CASCADE'),
        nullable=False
    )
    delivery_id = Column(
        Integer,
        ForeignKey('deliveries.id', ondelete='CASCADE'),
        nullable=False
    )
    status_id = Column(
        Integer,
        ForeignKey('order_status.id', ondelete='CASCADE'),
        default=0
    )
    created_at = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
