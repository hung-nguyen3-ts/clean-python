from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    id: int
    name: str
    price: float


class OrderLine(BaseModel):
    product: Product
    quantity: int

    @property
    def total_price(self) -> float:
        return self.product.price * self.quantity


class Order(BaseModel):
    id: int
    order_lines: List[OrderLine]

    user: User
    rider: Rider

    def calculate_total(self) -> float:
        return sum(line.total_price for line in self.order_lines)

    def validateOrder(self):
        self.user.validate()


Class Customer:
    def validateCustomer();


Class Agent:
