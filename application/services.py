from domain.entities import Order, OrderLine, Product
from domain.repository_interfaces import IOrderRepository
from application.utils import UnitOfWork
from infra.sql_repositories import SQLProductRepository, SqlOrderRepository


class OrderService:
    def __init__(self, uow: UnitOfWork, order_repository: IOrderRepository):
        self.uow = uow
        self.order_repository = order_repository
        self.customer


    def create_order(self, order_data) -> Order:
        customer = 3rdparty.get()
        rider = 3rdparty.get()
        with self.uow.start() as session:
            order_repo = self.order_repository(session)
            order_lines = [OrderLine(product=Product(**line['product']), quantity=line['quantity']) for line in order_data]
            order = Order(order_lines=order_lines, customer=customer)
            order.validatte()
            order_repo.add(order)
            return order

    def get_order_total(self, order_id: int) -> float:
        with self.uow.start() as session:
            order_repo = self.order_repository(session)
            order = order_repo.get(order_id)
            if not order:
                raise ValueError("Order not found")
            return order.calculate_total()

