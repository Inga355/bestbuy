from random import choice

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
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit\n")

        choice = input("Please make a choice: ")
        if choice == "1":
            for index, item in enumerate(your_store.get_all_products(), start=1):
                print(f"\n{index}.{item.show()}\n")
        elif choice == "2":
            print(f"\nTotal of {your_store.get_total_quantity()} items in store.\n")



start(best_buy)