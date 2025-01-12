class Store:
    """
    Class for building a store to handle products

    Attributes:
    list_of_products (list): list of products in store
    """

    def __init__(self, product_list):
        """
        Constructor for initializing the list of products in store
        """
        self.list_of_products = product_list


    def add_product(self, product):
        return self.list_of_products.append(product)


    def remove_product(self, product):
        return self.list_of_products.pop(product)


    def get_total_quantity(self) -> int:
        return sum(item.get_quantity() for item in self.list_of_products)


    def get_all_products(self) -> list:
        """
        returns a list of all active (available) products in store
        """
        active_products = []
        for item in self.list_of_products:
            if item.is_active():
                active_products.append(item)
        return active_products