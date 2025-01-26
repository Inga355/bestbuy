import pytest
from products import Product


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

    