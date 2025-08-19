"""
Delivery Route
"""
import logging
from app.services.order_data import OrderData
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from app.models.order_model import OrderCreate, OrderUpdate

router = APIRouter()


@router.post("/create")
async def create_order(order_obj: OrderCreate) -> JSONResponse:
    """
    Create Order Route
    :param order_obj:
    :return:
    """
    try:
        order_model = OrderData()
        row = order_model.create(
            status_id=order_obj.status_id,
            product_id=order_obj.product_id,
            delivery_id=order_obj.delivery_id,
            user_id=order_obj.user_id
        )
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Create user failed"
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": None,
                "error": False
            },
        )
    except HTTPException as e:
        logging.error("Order: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.get("/get/{order_id}")
async def get_order(order_id: int) -> JSONResponse:
    """
    Get User Route
    :param order_id:
    :return:
    """
    try:
        order_model = OrderData()
        row = order_model.get_one(order_id=order_id)
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get order failed"
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": row,
                "error": False
            },
        )
    except HTTPException as e:
        logging.error("Order: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.post("/update/{order_id}")
async def update_order(order_obj: OrderUpdate, order_id: int) -> JSONResponse:
    """
    Update Delivery Route
    :param order_obj:
    :param order_id:
    :return:
    """
    try:
        order_model = OrderData()
        row = order_model.update(
            order_id=order_id,
            status_id=order_obj.status_id,
            product_id=order_obj.product_id,
            delivery_id=order_obj.delivery_id,
            user_id=order_obj.user_id
        )
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get order failed"
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": None,
                "error": False
            },
        )
    except HTTPException as e:
        logging.error("Order: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.get("/")
async def get_all_orders() -> JSONResponse:
    """
    Get Orders Route
    :return:
    """
    try:
        order_model = OrderData()
        rows = order_model.get_all()
        if not rows:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get order failed"
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": {"orders": rows},
                "error": False
            },
        )
    except HTTPException as e:
        logging.error("Orders: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.post("/delete/{order_id}")
async def delete_user(order_id: int) -> JSONResponse:
    """
    Delete Delivery Route
    :param order_id:
    :return:
    """
    try:
        order_model = OrderData()
        row = order_model.delete(order_id=order_id)
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Delete order failed"
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": None,
                "error": False
            },
        )
    except HTTPException as e:
        logging.error("Order: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })
