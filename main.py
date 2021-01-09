
from pandas.tests.groupby.test_value_counts import df
from classes import Customer
import pandas as pd
from generate_customer_ID import get_random_string
from user_login import user_login

# User logs in with his credentials
user_login()

#a rondom customer string is generated
customer_id = get_random_string(int(input("Please enter the ID length (1-8): ")))

cus_id = []
name = []
address = []
date = []
amount = []
state = True
#create the first ID and customer details
customer = Customer(
        input("Please enter the customer name: "),
        input("Please enter the customer address: "),
        input("Please enter the order date: "),
        input("Please enter the order amount: "),

    )
#append the lists with customer details
cus_id.append(customer_id)
name.append(customer.name)
address.append(customer.address)
date.append(customer.date)
amount.append(customer.amount)

#place more orders
while state:
    # check if the user want to add another customer
    question = input("Want to add another customer?: yes/no: ")
    if question == "no":
            state = False
    if question == "yes":
        customer_id = get_random_string(int(input("Please enter the ID length (1-8): ")))
        customer = Customer(
            input("Please enter the customer name: "),
            input("Please enter the customer address: "),
            input("Please enter the order date: "),
            input("Please enter the order amount: "),

        )
        cus_id.append(customer_id)
        name.append(customer.name)
        address.append(customer.address)
        date.append(customer.date)
        amount.append(customer.amount)


# create a dictionary with customer attributes
customer_dict = {
    "customer_id": cus_id,
    "name": name,
    "address": address,
    "date": date,
    "amount": amount,
}

# create a dataframe in order to sort/coount/sum orders
customer_df = pd.DataFrame(customer_dict)
print(customer_df)





