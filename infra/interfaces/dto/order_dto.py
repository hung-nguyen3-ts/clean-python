from pydantic import BaseModel
from typing import List

class ProductDTO(BaseModel):
    id: int
    name: str
    price: float

class OrderLineDTO(BaseModel):
    product_id: int
    quantity: int

class CreateOrderRequest(BaseModel):
    order_lines: List[OrderLineDTO]
    riderId:

    def to_dto(self):
        pass

class OrderDTO(BaseModel):
    id: int
    order_lines: List[OrderLineDTO]