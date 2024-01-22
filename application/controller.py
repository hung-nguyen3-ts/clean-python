from application.dto import CreateOrderDto
from application.services import OrderService


class OrderController:
    _order_service: OrderService

    def __init__(
        self,
        order_service: OrderService,
    ):
        self._order_service = order_service

    async def create_order(self, create_order_dto: CreateOrderDto):
        return await self._order_service.create_order(create_order_dto)

    async def get_order_total(self, order_id):
        return await self._order_service.get_order_total(order_id)
