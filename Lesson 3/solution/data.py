class shoping:
    def __init__(self, name, rating=None, link=None, price=None, sale=False):
        self.rating = rating
        self.name: str = name
        self.link = link
        self.sale = sale
        self.price = price

    def __str__(self):
        return f"rating:{self.rating}\nname:{self.name}\nlink:{self.link}\nsale:{self.sale}\nprice:{self.price}"


def create_item(name) -> shoping:
    return shoping(name)


def set_rating(item: shoping, value):
    item.rating = value


def get_rating(item: shoping):
    return item.rating


def set_price(item: shoping, value):
    item.price = value


def get_price(item: shoping):
    return item.price


def set_name(item: shoping, value):
    item.name = value


def get_name(item: shoping):
    return item.name


def set_link(item: shoping, value):
    item.link = value


def get_link(item: shoping):
    return item.link


def set_sale(item: shoping, value):
    item.sale = value


def get_sale(item: shoping):
    return item.sale
