import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def start(your_store):
    """
    prints the store menu and asks for user choice
    has functionality for showing and buying products
    """
    while True:
        # Main Menu Loop, prints the Store Menu
        print("\n     STORE MENU")
        print("     ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit\n")

        # Gets the user choice from Store Menu
        choice = input("Please make a choice: ")

        # Lists all active products in shop
        if choice == "1":
            print("")
            for index, item in enumerate(your_store.get_all_products(), start=1):
                print(f"{index}.{item.show()}")
            print("")

        # Shows total amount of all products in store
        elif choice == "2":
            print(f"\nTotal of {your_store.get_total_quantity()} items in store.\n")

        # Prints list of available products
        elif choice == "3":
            while True:
                print("")
                for index, item in enumerate(your_store.get_all_products(), start=1):
                    print(f"{index}.{item.show()}")
                print("")
                print("When you want to finish order, enter empty text.")
                # Gets product number and amount from user or jumps back to store menu
                product_number = input("Which product # do you want? ")
                if product_number == "":
                    break
                product_number = int(product_number) -1
                quantity = int(input("What amount do you want? "))
                # Checks product number and amount of available items
                if 0 <= product_number < len(your_store.get_all_products()):
                    selected_product = your_store.get_all_products()[product_number]
                    if selected_product.get_quantity() >= quantity:
                        selected_product.buy(quantity)
                        print(f"\nOrdered {quantity} of {selected_product.name}. Remaining quantity: {selected_product.quantity}")
                    else:
                        print(f"\nNot enough quantity for {selected_product.name}. Available: {selected_product.quantity}")
                else:
                    print("Invalid product number. Please choose again.")

        # Quits the program
        elif choice == "4":
            break
        else:
            print("\nInvalid choice. Please try again.\n")


start(best_buy)