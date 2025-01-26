from itertools import product

import pytest
from products import Product, NonStockedProduct, LimitedProduct


def test_creating_product():
    product = Product("TestProduct", price=10.00, quantity=5)
    assert product.name == "TestProduct"
    assert product.price == 10.00
    assert product.quantity == 5
    assert product.active == True


def test_creating_product_with_zero_quantity():
    product = Product("TestProduct", price=10.00, quantity=0)
    assert product.name == "TestProduct"
    assert product.price == 10.00
    assert product.quantity == 0
    assert product.active == False


def test_creating_product_without_name():
    with pytest.raises(ValueError) as excinfo:
        Product(name="", price=10.00, quantity=5)
    assert "We need a name" in str(excinfo.value)


def test_creating_product_with_neg_price():
    with pytest.raises(ValueError) as excinfo:
        Product(name="TestProduct", price=-10.00, quantity=5)
    assert "Price needs to be higher than 0" in str(excinfo.value)


def test_creating_product_with_neg_quantity():
    with pytest.raises(ValueError) as excinfo:
        Product(name="TestProduct", price=10.00, quantity=-5)
    assert "Quantity cannot be negative" in str(excinfo.value)


def test_product_gets_deactivated():
    product = Product("TestProduct", price=10.00, quantity=5)
    product.set_quantity(-5)
    assert product.is_active() == False


def test_buying_to_much_raises_exception():
    product = Product("TestProduct", price=10.00, quantity=5)
    with pytest.raises(ValueError) as excinfo:
        product.buy(10)
    assert f"We don't have enough {product.name}. Only {product.quantity} left!" in str(excinfo.value)


def test_creating_subclass_NonStocked():
    product = NonStockedProduct(name="TestNonStocked", price=10.00)
    assert product.name == "TestNonStocked"
    assert product.price == 10.00
    assert product.active == True


def test_creating_subclass_LimitedProduct():
    product = LimitedProduct(name="TestLimited", price=10.00, quantity=5, maximum=1)
    assert product.name == "TestLimited"
    assert product.price == 10.00
    assert product.quantity == 5
    assert product.maximum == 1


def test_buying_more_than_maximum():
    product = LimitedProduct("TestProduct", price=10.00, quantity=5, maximum=1)
    with pytest.raises(ValueError) as excinfo:
        product.buy(3)
    assert f"You can only buy {product.maximum}."
