from promotions import Promotion


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
        self.promotion = None
        if quantity == 0:
            self.active = False
        else:
            self.active = True

    def get_price(self):
        return self.price

    def get_quantity(self) -> int:
        return self.quantity

    def get_promotion(self):
        return self.promotion

    def set_quantity(self, quantity) -> int:
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()
        return self.quantity

    def set_promotion(self, promotion: Promotion):
        self.promotion = promotion

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f" {self.name}, Price: {self.price}, Quantity: {self.quantity}, Promotion: {self.promotion}"

    def buy(self, quantity):
        """
        checks if product is available (quantity > 0) and
        changes the quantity of the product and returns the price to pay
        """
        if self.quantity < quantity:
            raise ValueError(f"We don't have enough {self.name}. Only {self.quantity} left!")
        if self.promotion:
            price_to_pay = self.promotion.apply_promotion(self, quantity)
        else:
            price_to_pay = quantity * self.price
        new_quantity = self.quantity - quantity
        self.set_quantity(new_quantity)
        print("Product added to list!")
        return price_to_pay


class NonStockedProduct(Product):
    """
    Subclass for products that have no quantity and are always available.
    """
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self.active = True

    def set_quantity(self, quantity) -> int:
        raise AttributeError("Cannot change the quantity of a non-stocked product.")

    def show(self):
        return f" {self.name}, Price: {self.price}, Promotion: {self.promotion}"

    def buy(self, quantity):
        """
        returns the price_to_pay
        """
        price_to_pay = quantity * self.price
        print("Product added to list!")
        return price_to_pay


class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        return f" {self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}, Promotion: {self.promotion}"

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"You can only buy {self.maximum}.")
        return super().buy(quantity)