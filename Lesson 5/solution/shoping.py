"""
This is the shopping object
author: Keegan Andrus
"""


class shoping:
    """ this is the shopping class/obj.
    This is where all attributes are stored about an object.
    """

    def __init__(
        self,
        name: str,
        rating: float | int = 0,
        link: str | None = None,
        price: float | None = None
    ):
        """__init__ initalizes the shopping class

        initailzes the shopping class and returns the shopping object.

        :param name: the item's name
        :type name: str
        :param rating: rating of the item, defaults to 0
        :type rating: float | int, optional
        :param link: link to the item, defaults to None
        :type link: str | None, optional
        :param price: price of the item, defaults to None
        :type price: float | None, optional
        :param sale: is item on sale, defaults to False
        :type sale: bool, optional
        """
        self.rating: str | int | float = rating
        """item rating"""
        self.name: str = name
        """item name"""
        self.link: str | None = link
        """item link"""
        self.sale: bool = False
        """is item on sale"""
        self.price: float | None = price
        """item price not including shipping fee"""
        self.rating_count: int = 0
        """how many ratings does the item have"""
        self.arival_date: str | int = ""
        """how many days will it take to arive"""
        self.delivery_cost: int | str | float = 0
        """cost of delivery"""
        self.source = ''
        """what is the name of the site ie: amazon"""

    def __float__(self):
        """Gets the cost

        if no price is set, 1000000.00 will be returned.
        delivery cost is included

        :return: cost to buy the item (price + shipping)
        :rtype: float
        """
        if isinstance(self.price, type(None)):
            return float(1000000)
        return float(self.price)+float(self.delivery_cost)

    def __str__(self):
        """user friendly output"""
        return f"""rating:{self.rating} | {self.rating_count}
    \nname:{self.name}
    \nprice:{float(self)}
    \n{self.arival_date}\n\n"""
