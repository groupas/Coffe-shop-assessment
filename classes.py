import string
from random import random

customer_total_orders = 0


class Customer:

    def __init__(self, name, address, date, amount):
        self.name = name
        self.address = address
        self.date = date
        self.amount = amount

# file = open()
#
# file.close()
