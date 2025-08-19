"""
Order Status Route
"""
import logging
from app.services.order_status_data import OrderStatusData
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from app.models.order_status_model import OrderStatusCreate, OrderStatusUpdate

router = APIRouter()


@router.post("/create")
async def create_order_status(order_status: OrderStatusCreate) -> JSONResponse:
    """
    Create Order Status Route
    :param order_status:
    :return:
    """
    try:
        order_status_model = OrderStatusData()
        row = order_status_model.create(status=order_status.status)
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Create order status failed"
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
        logging.error("Order status: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.get("/get/{order_status_id}")
async def get_order_status(order_status_id: int) -> JSONResponse:
    """
    Get Order Status Route
    :param order_status_id:
    :return:
    """
    try:
        order_status_model = OrderStatusData()
        row = order_status_model.get_one(order_status_id=order_status_id)
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get order status failed"
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
        logging.error("Order status: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.post("/update/{order_status_id}")
async def update_order_status(
        order_status: OrderStatusUpdate,
        order_status_id: int
) -> JSONResponse:
    """
    Update Order Status Route
    :param order_status:
    :param order_status_id:
    :return:
    """
    try:
        order_status_model = OrderStatusData()
        row = order_status_model.update(
            order_status_id=order_status_id,
            status=order_status.status
        )
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get order status failed"
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
        logging.error("Order status: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.get("/")
async def get_all_order_status() -> JSONResponse:
    """
    Get Orders Status Route
    :return:
    """
    try:
        order_status_model = OrderStatusData()
        rows = order_status_model.get_all()
        if not rows:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get orders status failed"
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
        logging.error("Order status: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.post("/delete/{order_status_id}")
async def delete_order_status(order_status_id: int) -> JSONResponse:
    """
    Delete Order Status Route
    :param order_status_id:
    :return:
    """
    try:
        order_status_model = OrderStatusData()
        row = order_status_model.delete(order_status_id=order_status_id)
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Delete order status failed"
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
        logging.error("Order status: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })
