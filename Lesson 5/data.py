"""
this is the interface for the shopping class/obj
author: Keegan Andrus
"""
import os
from datetime import datetime, date
import pandas as pd
from shoping import shoping


def get_dict(item: shoping) -> dict:
    """get_dict
    gets the dictionary representation of the item object

    :param item: the object that will be returned as a dict
    :type item: shoping
    :return: dict representation of `item`
    :rtype: dict
    """
    return item.__dict__


def create_item(name: str) -> shoping:
    """create_item initalizes the shopping object

    :param name: name of the item
    :type name: str
    :return: initalized shopping object
    :rtype: shoping
    """
    return shoping(name)


def set_rating(item: shoping, value: str):
    """set_rating saves the rating value to the `item`

    :param item: the shopping object
    :type item: shoping
    :param value: the rating value of the `item`
    :type value: str
    """
    item.rating = float(value.removesuffix(" out of 5 eggs"))


def get_rating(item: shoping) -> float:
    """get_rating returns the rating

    :param item: the shopping object
    :type item: shoping
    :return: the rating value of the `item`
    :rtype: float
    """
    return float(item.rating)


def set_price(item: shoping, value: str):
    """set_price sets the price for the `item`

    :param item: the shopping object
    :type item: shoping
    :param value: the price of the `item`
    :type value: str
    """
    item.price = float(value.removeprefix("$").replace(",", ""))


def get_price(item: shoping) -> float | None:
    """get_price gets the price of the `item`

    :param item: the shopping object
    :type item: shoping
    :return: the price value of the `item`
    :rtype: float | None
    """
    return item.price


def set_name(item: shoping, value: str):
    """set_name sets the name of the item


    :param item: the shopping object
    :type item: shoping
    :param value: the new name of the item
    :type value: str
    """
    item.name = value


def get_name(item: shoping) -> str:
    """get_name gets the name of the `item

    :param item: the shopping object
    :type item: shoping
    :return: the item name
    :rtype: str
    """
    return item.name


def set_link(item: shoping, value: str):
    """set_link sets the `item`'s link
    also sets the source from the link

    :param item: the shopping object
    :type item: shoping
    :param value: the link
    :type value: str
    """
    item.link = value
    item.source = value.split(".", 1)[-1].split(".", 1)[0]


def get_link(item: shoping) -> str | None:
    """get_link returns the `item`'s link

    :param item: the shopping object
    :type item: shoping
    :return: link of the `item`
    :rtype: str | None
    """
    return item.link


def set_sale(item: shoping, value: bool):
    """set_sale sets the bool of if the item is on sale or not

    :param item: the shopping object
    :type item: shoping
    :param value: true or false of if the item is on sale
    :type value: bool
    """
    item.sale = value


def get_sale(item: shoping) -> bool:
    """get_sale gets the status of if the item is on sale or not

    :param item: the shopping object
    :type item: shoping
    :return: true if on sale or false if not
    :rtype: bool
    """
    return item.sale


def set_rating_count(item: shoping, value: str):
    """set_rating_count sets the rating, must be a string input
    small level of data sanitization happens:
    - removes any comma prior to casting to int

    :param item: the shopping object
    :type item: shoping
    :param value: the count of how many times the item has been rated
    :type value: str
    """
    item.rating_count = int(value.replace(",", ""))


def get_rating_count(item: shoping) -> int:
    """get_rating_count gets the items rating count

    :param item: the shopping item
    :type item: shoping
    :return: the count of how many ratings have happened
    :rtype: int
    """
    return item.rating_count


def get_arival_date(item: shoping) -> str | int:
    """get_arival_date gets the count of how many days
    till the item will arive.

    returns a number if the input was in the date format, else returns `""`

    :param item: the shopping object
    :type item: shoping
    :return: "" or the number of days till it arives
    :rtype: str | int
    """
    return item.arival_date


def set_arival_date(item: shoping, value: str):
    """set_arival_date sets the `item`'s arival date.

    this is converted to the number of days till it arives
    if possible, if not, sets it to ""

    :param item: the shopping object
    :type item: shoping
    :param value: the arival date as seen in the web
    :type value: str
    """
    if value != "":
        item.arival_date = (datetime.strptime(
            f"{value} - {datetime.today().year}", "%A, %B %d - %Y").date() - date.today()).days
    else:
        item.arival_date = value


def get_delivery_cost(item: shoping) -> float | int | str:
    """get_delivery_cost gets the delivery cost of the item

    :param item: the shopping object
    :type item: shoping
    :return: how much it will cost to get the item delivered.
    :rtype: float | int | str
    """
    return item.delivery_cost


def set_delivery_cost(item: shoping, value: str):
    """set_delivery_cost sets the delivery cost.

    maps 'Free' to 0 and for all numbers, removes the '$' and any ','
    then casts it to a float

    :param item: the shopping object
    :type item: shoping
    :param value: the delivery cost as found on the web
    :type value: str
    """
    if value.upper() == 'FREE':
        value = "0"
    item.delivery_cost = float(value.removeprefix("$").replace(",", ""))


def get_best(*items: shoping) -> shoping:
    """get_best gets the best of the passed in shopping class objects

    merges the ratings and rating count
    rating is merged by weight.
    saves the details of the best to the data.json file

    :return: the best of the passed in shopping items
    :rtype: shoping
    """
    rating, count = zip(*[(x.rating, x.rating_count) for x in items])
    try:
        final_rating = sum(v * w for v, w in zip(rating, count))/sum(count)
    except ZeroDivisionError:
        final_rating = 0.0
    items_sorted = list(items)
    items_sorted.sort(key=float)
    set_rating(items_sorted[0], f"{final_rating}")
    set_rating_count(items_sorted[0], f"{sum(count)}")
    write_data(items_sorted[0])
    return items_sorted[0]


def write_data(item: None | shoping = None):
    """write_data saves the passed in item to the `data.json` file
    if the header does not exist then it will be created.

    calling this function without a shopping class object will erase the file


    :param item: the shopping class item. leave blank to reset file, defaults to None
    :type item: None | shoping, optional
    """
    if item is None:
        if os.path.exists("data.json"):
            os.remove('data.json')
        return
    df1 = pd.DataFrame([item.__dict__])
    if os.path.exists("data.json"):
        df = pd.read_json('data.json')
        df1 = pd.concat([df, df1], ignore_index=True)
        # df1 = df1.join(df)
    df1.to_json('data.json')
    return
