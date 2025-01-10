import products

class Store:

    def __init__(self, product_list):
        self.list_of_products = product_list

    def add_product(self, product):
        return self.list_of_products.append(product)

    def remove_product(self, product):
        return self.list_of_products.pop(product)

    def get_total_quantity(self) -> int:
        return len(self.list_of_products)

    def get_all_products(self) -> list:
        active_products = []
        for item in self.list_of_products:
            if item.is_active() == True:
                active_products.append(item)
        return active_products




product_list = [products.Product("MacBook Air M2", price=1450, quantity=0),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

store = Store(product_list)
products = store.get_all_products()
print(store.get_total_quantity())
print(store.get_all_products())
#print(store.order([(products[0], 1), (products[1], 2)]))