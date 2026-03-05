import pytest
from itemDetailsfunc import create_item, set_product_name, set_website_name, set_product_price, set_product_rating, set_product_shippingcost, set_product_brand
import itemDetailsfunc


@pytest.mark.parametrize("input_1, expected", [('flower', 'flower'), ('1', '1')])
def test_create_item(input_1, expected):
    myResult = create_item(input_1)
    assert myResult.item_to_search == expected


@pytest.mark.parametrize("input_1, expected", [('Google', 'Google'), ('0', '0')])
def test_set_website_name(input_1, expected):
    my_Obj = create_item("test")
    set_website_name(my_Obj, input_1)
    assert my_Obj.website_name == expected


@pytest.mark.parametrize("input_1, expected", [('Apple', 'Apple'), ('10', '10')])
def test_set_product_name(input_1, expected):
    my_Obj = create_item("test")
    set_product_name(my_Obj, input_1)
    assert my_Obj.product_name == expected


@pytest.mark.parametrize("input_1, expected", [('10.00', '10.00'), ('11', '11.00'), ('$12.00', '12.00'), ('abc13', '13.00'), ('010', '10.00')])
def test_set_product_price(input_1, expected):
    my_Obj = create_item("test")
    set_product_price(my_Obj, input_1)
    assert my_Obj.product_price == expected


@pytest.mark.parametrize("input_1, expected", [('10.00', '10.00'), ('11', '11.00'), ('$12.00', '12.00'), ('1,200', '1200'), ('Apple', '0')])
def test_set_product_shippingcost(input_1, expected):
    my_Obj = create_item("test")
    set_product_shippingcost(my_Obj, input_1)
    assert my_Obj.product_shippingcost == expected


@pytest.mark.parametrize("input_1, expected", [('10.00', '10.00'), ('2 out of 5', '12 out of 5')])
def test_set_product_rating(input_1, expected):
    my_Obj = create_item("test")
    set_product_rating(my_Obj, input_1)
    assert my_Obj.product_rating == expected


@pytest.mark.parametrize("input_1, expected", [('test', 'test'), ('6', '5')])
def test_set_product_brand(input_1, expected):
    my_Obj = create_item("test")
    set_product_brand(my_Obj, input_1)
    assert my_Obj.product_brand == expected
