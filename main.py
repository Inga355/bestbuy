import products
import promotions
import store
from products import NonStockedProduct, LimitedProduct


def start(your_store):
    """
    prints the store menu and asks for user choice
    has functionality for showing and buying products
    """
    # Maximum order counter for class "LimitedProduct"
    max_counter = 0

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
            total_price = 0
            while True:
                print("")
                for index, item in enumerate(your_store.get_all_products(), start=1):
                    print(f"{index}.{item.show()}")
                print("")
                print("When you want to finish order, enter empty text.")

                # Gets product number and amount from user or jumps back to store menu
                product_number = input("Which product # do you want? ")
                if product_number == "":
                    print("************************************")
                    print(f"Order made! Total payment: ${total_price}")
                    break
                product_number = int(product_number) -1
                quantity = int(input("What amount do you want? "))

                # Checks product number and amount of available items
                if 0 <= product_number < len(your_store.get_all_products()):
                    selected_product = your_store.get_all_products()[product_number]
                    # Check for critical purchase conditions
                    if selected_product.get_quantity() < quantity and not isinstance(selected_product, NonStockedProduct):
                        print(f"\nNot enough quantity for {selected_product.name}. Available: {selected_product.quantity}")
                    else:
                        # buys the product
                        if isinstance(selected_product, LimitedProduct):
                            try:
                                if (max_counter + quantity) > selected_product.maximum:
                                    raise ValueError(
                                        f"\nYou can only buy {selected_product.maximum} with this order.")
                            except ValueError as e:
                                print(e)
                                continue
                        item_costs = selected_product.buy(quantity)
                        if isinstance(selected_product, LimitedProduct):
                            max_counter += quantity
                        total_price += item_costs
                        print(f"\nOrdered {quantity} of {selected_product.name} for ${item_costs}. Remaining quantity: {selected_product.quantity}")
                else:
                    print("Invalid product number. Please choose again.")

        # Quits the program
        elif choice == "4":
            break
        else:
            print("\nInvalid choice. Please try again.\n")


def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()