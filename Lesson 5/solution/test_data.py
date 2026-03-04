from datetime import date
import data
import os
import pytest


@pytest.mark.parametrize("c_prefix", ["$", ""])
@pytest.mark.parametrize("cost",     [None, 100, 15.5, 15.36, 852.58])
@pytest.mark.parametrize("s_prefix", ["$", ""])
@pytest.mark.parametrize("shiping",  [None, 15.99, 68.00, 1.5, 52.48, "FREE"])
def test_data_init(c_prefix, cost, s_prefix, shiping):
    data_obj = data.create_item("test")
    total = 0
    if cost is not None:
        data.set_price(data_obj, f"{c_prefix}{cost}")
        total = cost
    else:
        # shiping_cost = shiping if shiping != 'FREE' else 0
        total = 1000000-[shiping, 0][shiping is None or shiping == 'FREE']
    if shiping is not None:
        if shiping == "FREE":
            data.set_delivery_cost(data_obj, f"{shiping}")
        else:
            data.set_delivery_cost(data_obj, f"{s_prefix}{shiping}")
            total += shiping
    FINAL_PRICE = data.get_price(data_obj) if data.get_price(

        data_obj) is not None else 1000000-data.get_delivery_cost(
            data_obj
    )  # pyright: ignore[reportOperatorIssue]
    val = FINAL_PRICE + data.get_delivery_cost(
        data_obj
    )  # pyright: ignore[reportOperatorIssue]

    assert float(data_obj) == val
    assert float(data_obj) == total, f"{float(data_obj)} != {total}"


@pytest.mark.parametrize("value,answer",     [
    ("5 out of 5 eggs", 5.0),
    ("5.0 out of 5 eggs", 5.0),
    ("3.7", 3.7),
    ("0.1", 0.1),
    ("3.7 out of 5 eggs", 3.7)
]
)
def test_rating(value: str, answer: float):
    data_obj = data.create_item("test")
    data.set_rating(data_obj, value)
    assert data.get_rating(data_obj) == answer


def test_rating_error():
    data_obj = data.create_item("test")
    with pytest.raises(AttributeError):
        data.set_rating(data_obj, None)  # pyright: ignore[reportArgumentType]
    data_obj.rating = None  # pyright: ignore[reportAttributeAccessIssue]
    with pytest.raises(TypeError):
        data.get_rating(data_obj)


@pytest.mark.parametrize("link", ["www.amazon.com", "www.amazon.ca", "www.newegg.com", "www.newegg.ca", "https://www.newegg.ca"])
def test_set_link(link):
    data_obj = data.create_item("test")
    assert data.get_link(data_obj) == None, "defalt not set"
    data.set_link(data_obj, link)
    assert data.get_link(data_obj) == link, "failed to set link"
    source = link.removeprefix(
        "https://").removeprefix("www.").removesuffix(".ca").removesuffix(".com")
    assert data_obj.source == source, "failed to set link"
    ""

# def test_set_link(link, source):


def test_rating_merge():
    # need to test with count of 0
    data_obj1 = data.create_item("test")
    data_obj2 = data.create_item("test")
    data.set_rating(data_obj1, "4.4")
    data.set_rating(data_obj2, "3.5")
    data.set_rating_count(data_obj1, "200")
    data.set_rating_count(data_obj2, "100")

    data_final = data.get_best(data_obj1, data_obj2)
    assert data.get_rating(data_final) == 4.1
    assert data.get_rating_count(data_final) == 300


@pytest.mark.parametrize("value1", [59.16, 2.77, 21.50, 18.26, 71.48, 47.98, 37.90, 62.15, 14.90, 30.47])
@pytest.mark.parametrize("value2", [2.30, 8.42, 59.49, 73.60, 25.51, 12.08, 36.55, 26.59, 49.13, 3.81])
# @pytest.mark.parametrize("value1", [1, 2, 3, 44, 5, 6, 7])
# @pytest.mark.parametrize("value2", [1, 2, 3, 44, 5, 6, 7])
def test_sorting_price(value1, value2):
    data_obj1 = data.create_item("test")
    data_obj2 = data.create_item("test")
    data.set_price(data_obj1, f"{value1}")
    data.set_price(data_obj2, f"{value2}")
    assert float(data.get_best(data_obj1, data_obj2)) == min(value1, value2)


@pytest.mark.parametrize("val", ["test1", "bob", "fan"])
def test_names(val):
    data_obj1 = data.create_item("test")
    assert data.get_name(data_obj1) == "test", "name set error on creation"
    data.set_name(data_obj1, val)
    assert data.get_name(data_obj1) == val, "set_name failed"


@pytest.mark.parametrize("value,answer,type_",     [
    (date.today().strftime("%A, %B %d"), 0, int),
    ("", "", str)
]
)
def test_arival_date(value, answer, type_):
    data_obj = data.create_item("test")
    data.set_arival_date(data_obj, value)
    assert isinstance(data.get_arival_date(data_obj), type_)
    assert data.get_arival_date(data_obj) == answer


def test_sale():
    data_obj = data.create_item("test")
    assert data.get_sale(data_obj) == False
    data.set_sale(data_obj, True)
    assert data.get_sale(data_obj) == True
    data.set_sale(data_obj, False)
    assert data.get_sale(data_obj) == False


def test_str_dict():
    data_obj = data.create_item("test")
    assert isinstance(str(data_obj), str)
    assert data_obj.__dict__ == data.get_dict(data_obj)


def test_writing():
    data.write_data()
    assert not os.path.exists("data.json")
    data_obj1 = data.create_item("test")
    data_obj2 = data.create_item("test")
    data.get_best(data_obj1, data_obj2)
    assert os.path.exists("data.json")
    data.write_data()
    assert not os.path.exists("data.json")
    data.write_data()
    assert not os.path.exists("data.json")
