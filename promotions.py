from abc import ABC, abstractmethod


class Promotion(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def apply_promotion(self, product, quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        product_to_pay_full = quantity // 2 + quantity % 2
        product_to_pay_half = quantity - product_to_pay_full
        return product.price * product_to_pay_full + product.price * 0.5 * product_to_pay_half


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        return product.price * quantity * ((100 - self.percent) / 100)


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        return product.price * (quantity - (quantity // 3))