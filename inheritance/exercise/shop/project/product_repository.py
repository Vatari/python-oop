from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for prod in self.products:
            if product_name == prod.name:
                return prod

    def remove(self, product_name: str):
        prod = self.find(product_name)
        if prod:
            self.products.remove(prod)

    def __repr__(self):
        result = []
        for prod in self.products:
            result.append(f"{prod.name}: {prod.quantity}")
        return '\n'.join(result)
