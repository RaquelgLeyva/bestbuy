from products import Product

class Store:

    def __init__(self, products):
        self.products = products


    def add_product(self, product):
       self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("The product is not in our stock.")

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self) -> list[Product]:
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self,shopping_list) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            try:
                price = product.buy(quantity)
                total_price += price
            except Exception as e:
                print(f"The {product.name} is not available: {e} ")
        return total_price



