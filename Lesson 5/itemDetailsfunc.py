import csv
from datetime import date, datetime, timedelta
import re


class itemDetails:
    def __init__(self, item_to_search, product_name=None, product_price=0, product_rating=None, product_shippingcost=0, website_name=None, product_brand=None, delivery_date=None, delivery_days=None):
        self.item_to_search = item_to_search
        self.product_name = product_name
        self.product_price: int | float = product_price
        self.product_rating = product_rating
        self.product_shippingcost: int | float = product_shippingcost
        self.website_name = website_name
        self.product_brand = product_brand
        self.delivery_date = delivery_date
        self.delivery_days = delivery_date


def create_item(item_to_search) -> itemDetails:
    return itemDetails(item_to_search)


def set_website_name(product: itemDetails, value):
    product.website_name = value


def set_product_name(product: itemDetails, value):
    product.product_name = value


def set_product_price(product: itemDetails, value):

    num_value = re.findall(r'\d+\.\d+|\d+', value)
    # value = value.replace("$", "").replace(",", "")
    num_value_float = float(num_value[0])
    product.product_price = num_value_float


def get_product_price(product: itemDetails):
    return product.product_price


def set_product_shippingcost(product: itemDetails, value):
    value = value.replace("$", "").replace(",", "")
    try:
        value = float(value)
    except:
        value = 0

    product.product_shippingcost = value


def set_product_rating(product: itemDetails, value):
    product.product_rating = value


def set_product_brand(product: itemDetails, value):
    product.product_brand = value


def get_details(product: itemDetails):

    return {"Productname": product.product_name,
            "Productprice": product.product_price,
            "ProductRating": product.product_rating}


def find_cheapest(dictForam: itemDetails, dictForne: itemDetails):
    amprice = dictForam.product_price + dictForam.product_shippingcost
    neprice = dictForne.product_price + dictForne.product_shippingcost
    # fieldnames = ['Productname', 'Productprice', 'ProductRating' ]
    # filename = 'Lesson 5\output.csv'

    if amprice > neprice:

        with open(r'Lesson 5\output.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            # Write the data rows
            writer.writerow([dictForne.website_name,
                             dictForne.product_name,
                             dictForne.product_price,
                             dictForne.product_shippingcost,
                             neprice,
                             dictForne.product_rating,
                             dictForne.product_brand])
    else:
        with open(r'Lesson 5\output.csv', 'a', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            # Write the data rows
            writer.writerow([dictForam.website_name,
                             dictForam.product_name,
                             dictForam.product_price,
                             dictForam.product_shippingcost,
                             amprice,
                             dictForam.product_rating,
                             dictForam.product_brand,
                             dictForam.delivery_date,
                             dictForam.delivery_days])


def clear_csv():
    with open(r'Lesson 5\output.csv', 'w', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['Best_Website',
                         'Product_name',
                         'Product_price',
                         'Product_shippingcost',
                         'Product_finalprice',
                         'ProductRating',
                         'Product_Brand',
                         'Delivery_date',
                         'Devivary_days'])


def set_date_of_delivery(product: itemDetails, value):
    product.delivery_date = value
    set_delivery_days(product)


def set_delivery_days(product: itemDetails):
    delivery_on = f"{product.delivery_date},{date.today().year}"
    parsed_date = datetime.strptime(delivery_on, "%A, %B %d,%Y").date()
    today = date.today()
    daydelta = parsed_date - today
    days_count = daydelta.days
    product.delivery_days = days_count
