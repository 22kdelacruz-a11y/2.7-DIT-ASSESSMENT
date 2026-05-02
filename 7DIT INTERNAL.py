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
custom = ["burrito", "bowl"]
wraps = ['tortilla', 'veggie tortilla', 'gluten-free tortilla']
proteins = ['steak', 'chicken', 'pork', 'veggie']
rices = ['white rice', 'brown rice', 'cilantro-lime rice']
beans = ['pinto beans', 'black beans', 'refried beans']
toppings = ['guacamole', 'sour cream', 'cheese', 'n/a']
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

def get_number():
    """a function to get the customer's phone number, this is used for both delivery and pick-up orders, this also checks if the input is valid and if it is not, it will ask the user to input again until they input a valid phone number"""
    while True:
        phone = input("Enter Phone Number (max 10 digits): ").strip()
        
        if not phone.isdigit():
            print("Error: Phone number must only contain digits.")
        
        elif len(phone) > 10:
            print(f"Error: Number is too long ({len(phone)} digits). Max is 10.")
        
        elif len(phone) < 7: 
            print("Error: Number is too short.")
        else:
            return phone

def add_order():
    """a function to add an order to the orders dictionary, this is where the user will input all of their order details and preferences"""
    print("--- Place Your Order---")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    while True: 
        choice = input("For delivery(1) or pick-up?(2): ")   
        if choice == "1":
            order_type = "Delivery"
            break
        elif choice == "2":
            order_type = "Pick-up"
            break
        else:
            print("Invalid input, Try again.")
    phone = get_number() 
    print("Now, let's build your order!")
    menu()
    menu_choice = input("Enter the number of the menu item you want to order: ")
    if menu_choice == "1":
        order_choice = input("Would you like to make a custom burrito or a custom burrito bowl? (Burrito/Bowl) ").lower()
        if order_choice not in custom:
            print("Invalid input, Try again.")
        if order_choice == "burrito":
            while True:
                burrito = "Custom Burrito"
                wrap_choice = input("Choose a wrap (tortilla, veggie tortilla, gluten-free tortilla): ").lower()
                if wrap_choice not in wraps:
                    print("Invalid wrap choice. Please try again.")
                else:
                    break
            while True:
                protein_choice = input("Choose a protein (steak, chicken, pork, veggie): ").lower()
                if protein_choice not in proteins:
                    print("Invalid protein choice. Please try again.")
                else:
                    break
            while True:
                rice_choice = input("Choose a rice (white rice, brown rice, cilantro-lime rice): ").lower()
                if rice_choice not in rices:
                    print("Invalid rice choice. Please try again.")
                else:
                    break
            while True:
                beans_choice = input("Choose a bean (pinto beans, black beans, refried beans): ").lower()
                if beans_choice not in beans:
                    print("Invalid bean choice. Please try again.")
                else:
                    break
            while True:
                topping_choice = input("Choose a topping (guacamole, sour cream, cheese, n/a): ").lower()
                if topping_choice not in toppings:
                    print("Invalid topping choice. Please try again.")
                else:
                    break
            orders[first_name] = {'first_name' : first_name,
                                'last_name' : last_name,
                                'order_type' : order_type,
                                'phone_number' : phone,
                                'order' : [burrito, wrap_choice, protein_choice, rice_choice, beans_choice, topping_choice]}
            print("Order placed successfully!")
            print(orders)
        elif order_choice == "bowl":
            bowl = "Custom Burrito Bowl"
            wrap_choice = "N/A"
            while True:
                protein_choice = input("Choose a protein (steak, chicken, pork, veggie): ").lower()
                if protein_choice not in proteins:
                    print("Invalid protein choice. Please try again.")
                else:
                    break
            while True:
                rice_choice = input("Choose a rice (white rice, brown rice, cilantro-lime rice): ").lower()
                if rice_choice not in rices:
                    print("Invalid rice choice. Please try again.")
                else:
                    break
            while True:
                beans_choice = input("Choose a bean (pinto beans, black beans, refried beans): ").lower()
                if beans_choice not in beans:
                    print("Invalid bean choice. Please try again.")
                else:
                    break
            while True:
                topping_choice = input("Choose a topping (guacamole, sour cream, cheese, n/a): ").lower()
                if topping_choice not in toppings:
                    print("Invalid topping choice. Please try again.")
                else:
                    break
            orders[first_name] = {'first_name' : first_name,
                                'last_name' : last_name,
                                'order_type' : order_type,
                                'phone_number' : phone,
                                'order' : [bowl, wrap_choice, protein_choice, rice_choice, beans_choice, topping_choice]}
            print("Order placed successfully!")
            print(orders) # CHANGE FORMATTING LATER
        else:
            print("Invalid input, Try again.")
    print(f"Thank you for your order, {first_name}! Your order details are as follows:")
    print(f"Name: {first_name} {last_name}")
    print(f"Order Type: {order_type}")
    print(f"Phone Number: {phone}")
    print(f"Wrap: {orders[first_name]['order'][1]}")
    print(f"Protein: {orders[first_name]['order'][2]}")
    print(f"Rice: {orders[first_name]['order'][3]}")
    print(f"Beans: {orders[first_name]['order'][4]}")
    print(f"Topping: {orders[first_name]['order'][5]}")

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
            add_order()
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