# repository_interfaces.py
from abc import ABC, abstractmethod
from typing import List, Optional
from entities import Product, Order


class IProductRepository(ABC):
    @abstractmethod
    def add(self, product: Product) -> None:
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def list(self) -> List[Product]:
        pass


class IOrderRepository(ABC):

    @abstractmethod
    def add(self, order: Order) -> None:
        """Add a new order to the repository."""
        pass

    @abstractmethod
    def get_by_id(self, order_id: int) -> Optional[Order]:
        """Retrieve an order by its ID."""
        pass