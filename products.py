class Product:

    def __init__(self, name, price, quantity):
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
        print(f"----------------------")
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")

    def buy(self, quantity):
        if self.quantity < quantity:
            raise ValueError(f"We don't have enough {self.name}. Only {self.quantity} left!")
        new_quantity = self.quantity - quantity
        return self.set_quantity(new_quantity)

