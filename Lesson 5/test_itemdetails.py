import pytest
from itemDetailsfunc import create_item, set_product_name, set_website_name, set_product_price, set_product_rating, set_product_shippingcost


@pytest.mark.parametrize("input_1, expected", [('flower', 'flower'), ('1', '1')])
def test_create_item(input_1, expected):
    myResult = create_item(input_1)
    assert myResult.item_to_search == expected


@pytest.mark.parametrize("input_1, expected", [('Google', 'Google'), ('0', '0')])
def test_set_website_name(input_1, expected):
    myResult = create_item(input_1)
    assert myResult.website_name == expected


@pytest.mark.parametrize("input_1, expected", [('Apple', 'Apple'), ('10', '10')])
def test_set_product_name(input_1, expected):
    myItem = create_item(input_1)
    assert myItem.item_to_search == expected


@pytest.mark.parametrize("input_1, expected", [('10.00', '10.00'), ('11', '11.00'), ('$12.00', '12.00'), ('abc13', '13.00'), ('010', '10.00')])
def test_set_product_price(input_1, expected):
    myItem = create_item(input_1)
    assert myItem.item_to_search == expected

# def test_set_product_name():
    # assert False
