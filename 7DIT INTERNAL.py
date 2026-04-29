#LISTS 
admin_password = "pw"
orders = {'Kian' : {'first_name' : 'Kian',
                    'last_name' : 'Dela Cruz',
                    'order_type' : 'Pick-up',
                    'phone_number' : '123123123',
                    'order' : ['Custom Burrito','Tortilla','Steak','White Rice','Pinto Beans','Guacamole','N/A']},
                    
          'Nhico' : {'first_name' : 'Nhico',
                     'last_name' : 'Bigcas',
                     'order_type' : 'Delivery',
                     'phone_number' : '321321321',
                     'order' : ['Custom Burrito Bowl','N/A','Chicken','Brown Rice','Black Beans','Sour Cream','Cheese']}}

#FUNCTIONS
def menu():                               
    """displays numbered menu"""
    print(" ----------------------")
    print("│ 1 - Make your own!   │ ")
    print("│ 2 - Nachorrrito      │ ")
    print("│ 3 - Special Bowl!!!  │ ")
    print("│ 4 - Mad Salad        │ ")
    print("│ 5 - Tacos            │ ")
    print("│ 6 - Quesadillas      │ ")

def view_info():
    """displays the info about the restaurant"""
    print("""XXX is a restaurant chain based in YYY, XXX is full of balbalbal
dasdawd""")

def customer_program():
    """displays the different options the user could do if they had chose the customer program"""
    print("What would you like to do?")
    print("1. View menu.")
    print("2. Order.")
    print("3. View Info.")
    print("4. Exit.")

def admin_program():
    print("What would you like to do?")
    print("1. View orders.")
    print("2. Cancel orders.")
    print("3. Confirm orders.")
    print("4. Exit")

def get_user():  
    """a function to check if the one handling the website is a customer or an employee/staff"""
    print()
    print("               -------------------------")
    print("Welcome to n/a! Are you the admin or a customer?")
    while True:
        user = input(": ").lower()   # all of the printed statements are temporary
        if user == "customer":
            return user
        elif user == "admin":
            print()
            print("In order to access the admin account, you would need to enter a password. To return, input X.")      # password system
            pw_input = input("Enter the password: ").lower()     
            if pw_input == admin_password:
                print()
                print("               -------------------------")
                print("Welcome!")
                return user
            if pw_input == "x":
                print()
                print("               -------------------------")
                print("Welcome to n/a! Are you  the admin or a customer?")
                continue
            else:
                print()
                print("Incorrect password. Try again.")
                print("Welcome to n/a! Are you  the admin or a customer?")
        else:
            print()
            print('You must input either "Customer" or "Admin", Try again.')

#START OF THE PROGRAM

user = get_user()

if user == "customer":
    print("               -------------------------")
    print("Welcome to xxx!")
    while True:
        customer_program()
        customer_input = input(": ")
        if customer_input == "1":
            menu()
        elif customer_input == "2":
            pass
        elif customer_input == "3":
            view_info()
        elif customer_input == "4":
            break
        else:
            print("Invalid input, Try again.")

if user == "admin":
    while True:
        admin_program()
        admin_input = input(": ")
        if admin_input == "1":
            pass
        elif admin_input == "2":
            pass
        elif admin_input == "3":
            pass
        elif admin_input == "4":
            break
        else:
            print("Invalid input, Try again.")