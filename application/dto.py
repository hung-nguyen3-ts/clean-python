from typing import List


class ProductDTO(BaseModel):
    id: int
    name: str
    price: float

class OrderLineDTO(BaseModel):
    product_id: int
    quantity: int

class CreateOrderDto(BaseModel):
    order_lines: List[OrderLineDTO]
    rider
    def from_request(self, request):
#         convert from request to dto
       pass

class OrderDTO(BaseModel):
    id: int
    order_lines: List[OrderLineDTO]