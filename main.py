import products
from store import Store


product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = Store(product_list)
all_products = best_buy.get_all_products()

def start(store):
    """Starts the menu loop for the user to interact with the store."""

    while True:
        # Display the menu
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        # User input for menu option
        user_input = input("Please choose a number: ")

        if user_input == "1":
            # Option 1: List all products
            print("List all products in store:")
            for product in store.get_all_products():
                print(f"{product.name}, Price: ${product.price}, Quantity: {product.quantity}")

        elif user_input == "2":
            # Option 2: Show total quantity of products in store
            print("Show total amount in store:")
            print(store.get_total_quantity())

        elif user_input == "3":
            # Option 3: Make an order
            print("Make an order.")
            shopping_list = []  # Empty list to store the products for the order

            # Show available products
            print("\nAvailable products:")
            for idx, product in enumerate(store.get_all_products(), start=1):
                print(f"{idx}. {product.name}, Price: ${product.price}")

            # Product selection
            product_choice = input("Enter product number: ")
            if not product_choice.isdigit() or int(product_choice) < 1 or int(product_choice) > len(store.get_all_products()):
                print("Invalid choice! Try again.")
                continue

            product = store.get_all_products()[int(product_choice) - 1]  # Get the selected product

            # Quantity selection
            quantity = input(f"How many {product.name} do you want? ")
            if not quantity.isdigit() or int(quantity) <= 0:
                print("Invalid quantity! Try again.")
                continue

            quantity = int(quantity)
            if quantity > product.quantity:
                print(f"Not enough stock for {product.name}. Try again.")
                continue

            # Add product to order
            shopping_list.append((product, quantity))
            print(f"Added {quantity} {product.name} to your order.")

            # Finalize order
            total_price = 0
            for product, quantity in shopping_list:
                total_price += product.price * quantity
            print(f"Order completed! Total payment: ${total_price}")
            return total_price

        elif user_input == "4":
            print("Quitting...")
            break  # Exit the loop

        else:
            print("Invalid option! Try again.")

start(best_buy)










