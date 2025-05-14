class Product:
    def __init__(self, name, price, quantity):
        """Initialize a new product with a name, price, and quantity."""
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be less than 1 or a negative number.")
        if quantity < 0:
            raise ValueError("Quantity cannot be less than 1 or a negative number.")
        self.name = name  # str
        self.price = price  # float
        self.quantity = quantity  # int
        self.active = True  # bool: Whether the product is active and available for sale.

    def get_quantity(self) -> int:
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set a new quantity for the product and deactivate if quantity is zero."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()  # Deactivate if quantity reaches zero.
        else:
            self.activate()  # Activate if quantity is more than zero.

    def is_active(self) -> bool:
        """Return whether the product is active."""
        return self.active

    def activate(self):
        """Activate the product, making it available for sale."""
        self.active = True

    def deactivate(self):
        """Deactivate the product, making it unavailable for sale."""
        self.active = False

    def show(self) -> str:
        """Return a string representation of the product with its details."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """Buy a product, decreasing its stock and returning the total price."""
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()  # Deactivate if no stock left.
        return self.price * quantity
