from pandas.tests.indexing.multiindex.test_indexing_slow import a, b

granted = False
option = ""
def user_login():
    def grant():
        global granted
        granted = True
    def login(name, password):
        success = False
        file = open("C:\\Users\\giorg\\PycharmProjects\\pythonProject7\\user_details.txt", "r")
        for i in file:
            if(a==name , b ==password):
                success = True
                break
        file.close()
        if(success):
            print("Log in successful")
            grant()
        else:
            print("Wrong username or password")
    def register(name, password):
        file = open("C:\\Users\\giorg\\PycharmProjects\\pythonProject7\\user_details.txt", "a")
        file.write("\n"+name+","+password)
        file.close()
        grant()
        print("Registration Success")
    def access(option):
        global name
        if(option == "login"):
            name = input("Please enter your user name: ")
            password = input("Please enter your password: ")
            login(name, password)
        elif(option == "reg"):
            print("Enter Please enter your user name and password to register: ")
            name = input("Please enter your user name: ")
            password = input("Please enter your password: ")
            register(name, password)
    def begin():
        global option
        print("Welcome to Coffeeshop")
        option = input("Login or Register (login, reg): ")
        if option != "login" and option != "reg":
            begin()
    begin()
    access(option)




