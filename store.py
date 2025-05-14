from products import Product

class Store:
    def __init__(self, products):
        """Initialize the store with a list of products."""
        self.products = products  # List of Product objects.

    def add_product(self, product):
        """Add a new product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("The product is not in our stock.")

    def get_total_quantity(self) -> int:
        """Return the total quantity of all products in the store."""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity  # Add quantity of each product.
        return total_quantity

    def get_all_products(self) -> list[Product]:
        """Return a list of all active products in the store."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        """Process an order and return the total price."""
        total_price = 0
        for product, quantity in shopping_list:
            try:
                price = product.buy(quantity)
                total_price += price
            except Exception as e:
                print(f"The {product.name} is not available: {e} ")
        return total_price
