import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def start(your_store):
    while True:
        print("\n     STORE MENU")
        print("     ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit\n")

        choice = input("Please make a choice: ")

        if choice == "1":
            print("")
            for index, item in enumerate(your_store.get_all_products(), start=1):
                print(f"{index}.{item.show()}")
            print("")

        elif choice == "2":
            print(f"\nTotal of {your_store.get_total_quantity()} items in store.\n")

        elif choice == "3":
            print("")
            for index, item in enumerate(your_store.get_all_products(), start=1):
                print(f"{index}.{item.show()}")
            print("")
            print("When you want to finish order, enter empty text.")

            product_number = input("Which product # do you want? ")
            if product_number == "":
                continue

            product_number = int(product_number) -1
            quantity = int(input("What amount do you want? "))

            if 0 <= product_number < len(your_store.get_all_products()):
                selected_product = your_store.get_all_products()[product_number]
                if selected_product.get_quantity() >= quantity:
                    selected_product.buy(quantity)
                    print(f"Ordered {quantity} of {selected_product.name}. Remaining quantity: {selected_product.quantity}")
                else:
                    print(f"Not enough quantity for {selected_product.name}. Available: {selected_product.quantity}")
            else:
                print("Invalid product number. Please choose again.")

        elif choice == "4":
            break
        else:
            print("\nInvalid choice. Please try again.\n")


start(best_buy)