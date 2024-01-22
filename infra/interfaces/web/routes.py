from fastapi import FastAPI, HTTPException
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends, File, UploadFile

from application.controller import OrderController
from infra.interfaces.dto.order_dto import CreateOrderRequest, OrderDTO
from infra.interfaces.fastapi_routes import app


@app.post("/orders/", response_model=OrderDTO)
@inject
def create_order(request: CreateOrderRequest, order_controller: OrderController = Depends(Provide["order_controller"])):
    try:
        create_order_dto = request.to_dto()
        order = order_controller.create_order(create_order_dto)
        return order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/orders/{order_id}/total")
@inject
async def get_order_total(order_id: int, order_controller: OrderController = Depends(Provide["order_controller"])):
    try:
        total = order_controller.get_order_total(order_id)
        return {"order_id": order_id, "total": total}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
