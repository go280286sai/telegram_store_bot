"""
Delivery Route
"""
import logging
from app.services.delivery_data import DeliveryData
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from app.models.delivery_model import DeliveryCreate, DeliveryUpdate

router = APIRouter()


@router.post("/create")
async def create_delivery(delivery_obj: DeliveryCreate) -> JSONResponse:
    """
    Create Delivery Route
    :param delivery_obj:
    :return:
    """
    try:
        delivery_model = DeliveryData()
        row = delivery_model.create(
            name=delivery_obj.name,
            description=delivery_obj.description
        )
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Create delivery failed"
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
        logging.error("Delivery: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.get("/get/{delivery_id}")
async def get_delivery(delivery_id: int) -> JSONResponse:
    """
    Get User Route
    :param delivery_id:
    :return:
    """
    try:
        delivery_model = DeliveryData()
        row = delivery_model.get_one(delivery_id=delivery_id)
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get delivery failed"
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
        logging.error("Delivery: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.post("/update/{delivery_id}")
async def update_user(
        delivery_obj: DeliveryUpdate,
        delivery_id: int
) -> JSONResponse:
    """
    Update Delivery Route
    :param delivery_id:
    :param delivery_obj:
    :return:
    """
    try:
        delivery_model = DeliveryData()
        row = delivery_model.update(
            delivery_id=delivery_id,
            description=delivery_obj.description,
            name=delivery_obj.name
        )
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get delivery failed"
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
        logging.error("Delivery: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.get("/")
async def get_all_deliveries() -> JSONResponse:
    """
    Get Deliveries Route
    :return:
    """
    try:
        delivery_model = DeliveryData()
        rows = delivery_model.get_all()
        if not rows:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get delivery failed"
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": {"deliveries": rows},
                "error": False
            },
        )
    except HTTPException as e:
        logging.error("Delivery: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.post("/delete/{delivery_id}")
async def delete_user(delivery_id: int) -> JSONResponse:
    """
    Delete Delivery Route
    :param delivery_id:
    :return:
    """
    try:
        delivery_model = DeliveryData()
        row = delivery_model.delete(delivery_id=delivery_id)
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Delete delivery failed"
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
        logging.error("Delivery: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })
