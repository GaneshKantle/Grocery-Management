class GroceryStoreInventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, name, quantity, price):
        if name in self.inventory:
            print("Item already exists. Use update option to modify quantity.")
        else:
            self.inventory[name] = {'quantity': quantity, 'price': price}
            print(f"Item '{name}' added to the inventory.")

    def update_quantity(self, name, quantity):
        if name in self.inventory:
            self.inventory[name]['quantity'] += quantity
            print(f"Quantity for item '{name}' updated to {self.inventory[name]['quantity']}.")
        else:
            print("Item not found. Use add option to add a new item.")

    def view_inventory(self):
        print("\nCurrent Inventory:")
        for item, details in self.inventory.items():
            print(f"Item: {item}, Quantity: {details['quantity']}, Price: {details['price']:.2f}")

    def remove_item(self, name):
        if name in self.inventory:
            del self.inventory[name]
            print(f"Item '{name}' removed from the inventory.")
        else:
            print("Item not found.")

def main():
    grocery_store = GroceryStoreInventory()

    while True:
        print("\nMenu:")
        print("1. Add new item")
        print("2. Update item quantity")
        print("3. View inventory")
        print("4. Remove item")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity =(input("Enter quantity: "))
            price = float(input("Enter price per unit: "))
            grocery_store.add_item(name, quantity, price)

        elif choice == '2':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity to add (use negative value to subtract): "))
            grocery_store.update_quantity(name, quantity)

        elif choice == '3':
            grocery_store.view_inventory()

        elif choice == '4':
            name = input("Enter item name to remove: ")
            grocery_store.remove_item(name)

        elif choice == '5':
            print("Exiting program. Thank you!")
            break

        else:
            
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
