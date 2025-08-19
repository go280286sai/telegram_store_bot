"""
User Route
"""
import logging
from app.services.users_data import UsersData
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from app.models.user_model import UserUpdate, UserCreate

router = APIRouter()


@router.post("/create")
async def create_order_status(user_obj: UserCreate) -> JSONResponse:
    """
    Create Order Status Route
    :param user_obj:
    :return:
    """
    try:
        user_model = UsersData()
        row = user_model.create(name=user_obj.name, username=user_obj.username)
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
        logging.error("User: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.get("/get/{user_id}")
async def get_user(user_id: int) -> JSONResponse:
    """
    Get User Route
    :param user_id:
    :return:
    """
    try:
        user_model = UsersData()
        row = user_model.get_one(user_id=user_id)
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get user failed"
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
        logging.error("User: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.post("/update/{user_id}")
async def update_user(user_obj: UserUpdate, user_id: int) -> JSONResponse:
    """
    Update User Route
    :param user_id:
    :param user_obj:
    :return:
    """
    try:
        user_model = UsersData()
        row = user_model.update(
            user_id=user_id,
            username=user_obj.username,
            name=user_obj.name
        )
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get user failed"
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
        logging.error("User: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.get("/")
async def get_all_users() -> JSONResponse:
    """
    Get Users Route
    :return:
    """
    try:
        user_model = UsersData()
        rows = user_model.get_all()
        if not rows:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Get user failed"
            )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": True,
                "data": {"users": rows},
                "error": False
            },
        )
    except HTTPException as e:
        logging.error("User status: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })


@router.post("/delete/{user_id}")
async def delete_user(user_id: int) -> JSONResponse:
    """
    Delete User Route
    :param user_id:
    :return:
    """
    try:
        user_model = UsersData()
        row = user_model.delete(user_id=user_id)
        if not row:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Delete user failed"
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
        logging.error("User: %s" % e.detail)
        return JSONResponse(
            status_code=e.status_code,
            content={
                "success": False,
                "data": None,
                "error": e.detail
            })
