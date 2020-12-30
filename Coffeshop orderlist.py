#import users
#import sys

#user1 = sys.argv[1]
#print(user1)

#After each order placed the user will enter to the system:
#•	The name of the customer
#•	Address of the customer
#•	Date (DDMMYY)
#•	Total amount of order

def UserInput():

    Totalorders = 0
    Orderlist = ["name", "address", "date", "totalamount"]

    Orderlist[0] = input("Please enter the name of the customer: ")
    Orderlist[1] = input("Please enter the address of the customer: ")
    Orderlist[2] = input("Please enter the date of the order: ")
    Orderlist[3] = input("Please enter the total amount of the order: ")
    print(Orderlist)

    userId = str(Orderlist[0])    #user Id is generated for each customer
    print("User ID is: ", userId)

    Totalorders= Totalorders + 1   #total orders made by the customer
    print("Total orders: ", Totalorders)
UserInput()