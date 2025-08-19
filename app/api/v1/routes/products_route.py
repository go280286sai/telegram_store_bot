"""
Product Route
"""
import logging
from app.services.product_data import ProductData
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from app.models.products_model import ProductUpdate, ProductCreate

router = APIRouter()


@router.post("/create")
async def create_product(product_obj: ProductCreate) -> JSONResponse:
    """
    Create Product Route
    :param product_obj:
    :return:
    """
    try:
        product_model = ProductData()
        row = product_model.create(
            name=product_obj.name,
            description=product_obj.description,
            price=product_obj.price,
            amount=product_obj.amount,
            is_service=product_obj.is_service
        )
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Create product failed"
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
        logging.error("Product: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.get("/get/{product_id}")
async def get_product(product_id: int) -> JSONResponse:
    """
    Get User Route
    :param product_id:
    :return:
    """
    try:
        product_model = ProductData()
        row = product_model.get_one(product_id=product_id)
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get product failed"
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
        logging.error("Product: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.post("/update/{product_id}")
async def update_product(
        product_obj: ProductUpdate,
        product_id: int
) -> JSONResponse:
    """
    Update Product Route
    :param product_obj:
    :param product_id:
    :return:
    """
    try:
        product_model = ProductData()
        row = product_model.update(
            product_id=product_id,
            name=product_obj.name,
            description=product_obj.description,
            price=product_obj.price,
            amount=product_obj.amount,
            is_service=product_obj.is_service
        )
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get product failed"
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
        logging.error("Product: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.get("/")
async def get_all_products() -> JSONResponse:
    """
    Get Products Route
    :return:
    """
    try:
        product_model = ProductData()
        rows = product_model.get_all()
        if not rows:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get products failed"
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": {"products": rows},
                "error": False
            },
        )
    except HTTPException as e:
        logging.error("Product: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.post("/delete/{product_id}")
async def delete_user(product_id: int) -> JSONResponse:
    """
    Delete Delivery Route
    :param product_id:
    :return:
    """
    try:
        product_model = ProductData()
        row = product_model.delete(product_id=product_id)
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Delete product failed"
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
        logging.error("Product: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })
