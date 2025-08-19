import uvicorn
from fastapi import FastAPI
from app.api.v1.routes import (order_status_route,
                               users_route, delivery_route,
                               products_route, order_route)
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename="debug.log",
    filemode="w"
)

app = FastAPI()
app.include_router(
    order_status_route.router,
    prefix="/order_statuses",
    tags=["order_statuses"]
)
app.include_router(
    users_route.router,
    prefix="/users",
    tags=["users"]
)
app.include_router(
    delivery_route.router,
    prefix="/deliveries",
    tags=["deliveries"]
)
app.include_router(
    products_route.router,
    prefix="/products",
    tags=["products"]
)
app.include_router(
    order_route.router,
    prefix="/orders",
    tags=["orders"]
)


@app.get("/")
async def root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
