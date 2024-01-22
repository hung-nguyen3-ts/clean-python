from typing import List, Optional

from domain.entities import Order
from domain.repository_interfaces import IProductRepository, IOrderRepository
from sqlalchemy.orm import Session
from domain.model.entities import Product


class SQLProductRepository(IProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, product: Product) -> None:
        self.session.add(product)
        self.session.commit()

    def get_by_id(self, product_id: int) -> Product:
        return self.session.query(Product).filter_by(id=product_id).first()

    def list(self) -> List[Product]:
        return self.session.query(Product).all()


class SqlOrderRepository(IOrderRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, order: Order) -> None:
        self.session.add(order)

    def get_by_id(self, order_id: int) -> Optional[Order]:
        return self.session.query(Order).filter_by(id=order_id).one_or_none()
