from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract class to add special price calculation to a product
    """
    @abstractmethod
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def apply_promotion(self, product, quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    """
    Subclass to get every second item at half price
    """
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        product_to_pay_full = quantity // 2 + quantity % 2
        product_to_pay_half = quantity - product_to_pay_full
        return product.price * product_to_pay_full + product.price * 0.5 * product_to_pay_half


class PercentDiscount(Promotion):
    """
    Subclass to get percentage discount (i.e. 20% off)
    """
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        return product.price * quantity * ((100 - self.percent) / 100)


class ThirdOneFree(Promotion):
    """
    Subclass to buy 2 and get one free
    """
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        return product.price * (quantity - (quantity // 3))