class Supermarket:
    def __init__(self):
        # Initialize an empty list for cart items
        self.cart = []

    def add_item(self, name, price, quantity):
        """Add an item to the cart."""
        item = {
            'name': name,
            'price': price,
            'quantity': quantity,
            'total': price * quantity
        }
        self.cart.append(item)
        print(f"Added {quantity} x {name} (Price: {price} each) to the cart.")

    def calculate_total(self):
        """Calculate the total cost of items in the cart."""
        total = sum(item['total'] for item in self.cart)
        return total

    def apply_tax(self, total, tax_rate):
        """Apply tax to the total amount."""
        tax = total * (tax_rate / 100)
        return total + tax, tax

    def generate_bill(self, tax_rate=5.0):
        """Generate and print the bill."""
        print("\n===== Supermarket Bill =====")
        print(f"{'Item':<20} {'Price':<10} {'Quantity':<10} {'Total':<10}")
        print("-" * 50)

        for item in self.cart:
            print(f"{item['name']:<20} {item['price']:<10} {item['quantity']:<10} {item['total']:<10}")

        total = self.calculate_total()
        total_with_tax, tax_amount = self.apply_tax(total, tax_rate)

        print("-" * 50)
        print(f"{'Total (without tax)':<40} {total:<10}")
        print(f"{'Tax ({tax_rate}%):':<40} {tax_amount:<10}")
        print(f"{'Total (with tax)':<40} {total_with_tax:<10}")
        print("=" * 50)
        print("Thank you for shopping with us!")

    def show_menu(self):
        """Display the menu options for the user."""
        print("\n===== Supermarket Menu =====")
        print("1. Add Item to Cart")
        print("2. Generate Bill")
        print("3. Exit")

    def run(self):
        """Run the supermarket bill generation system."""
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                name = input("Enter item name: ")
                try:
                    price = float(input("Enter item price: "))
                    quantity = int(input("Enter quantity: "))
                    self.add_item(name, price, quantity)
                except ValueError:
                    print("Invalid price or quantity. Please enter valid numbers.")
            elif choice == "2":
                tax_rate = float(input("Enter tax rate (default 5%): ") or 5.0)
                self.generate_bill(tax_rate)
            elif choice == "3":
                print("Exiting the system. Thank you!")
                break
            else:
                print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    supermarket = Supermarket()
    supermarket.run()
