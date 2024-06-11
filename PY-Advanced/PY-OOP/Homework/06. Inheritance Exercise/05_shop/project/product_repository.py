from typing import List, Optional
from project.product import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, name: str) -> Optional[Product]:
        res = [p for p in self.products if p.name == name]
        if res:
            return res[0]

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)
        self.products.remove(product)

    def __repr__(self) -> str:
        return "\n".join([f"{p.name}: {p.quantity}" for p in self.products])
