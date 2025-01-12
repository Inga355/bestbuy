class Product:
    """
    Class for adding a product to the store

    Attributes:
    name (str): product name
    price (float): product price
    quantity (int): amount of available products in store
    """


    def __init__(self, name, price, quantity):
        """
        Constructor for name, price and quantity initialisation of a product
        """
        if not name:
            raise ValueError("We need a name")
        if price <= 0:
            raise ValueError("Price needs to be higher than 0")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.name = name
        self.price = price
        self.quantity = quantity
        if quantity == 0:
            self.active = False
        else:
            self.active = True


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.active = False
        else:
            return self.quantity


    def is_active(self) -> bool:
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        return f" {self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """
        checks if product is available (quantity > 0) and
        changes the quantity of the product
        """
        if self.quantity < quantity:
            raise ValueError(f"We don't have enough {self.name}. Only {self.quantity} left!")
        new_quantity = self.quantity - quantity
        return self.set_quantity(new_quantity)


