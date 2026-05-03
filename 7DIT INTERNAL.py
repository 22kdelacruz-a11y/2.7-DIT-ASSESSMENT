"""This file is a program that simulates a restaurant ordering system for a restaurant called Tortios. The program allows customers to view the menu, place orders, and view information about the restaurant."""
orders = {}
custom = ["burrito", "bowl"]
wraps = ['Tortilla', 'Veggie', 'Cassava']
proteins = ['Steak', 'Chicken', 'Pork', 'Veggie']
rices = ['White', 'Brown', 'Black']
beans = ['Pinto', 'Black', 'Refried']
toppings = ['Guacamole', 'Sour Cream', 'Cheese', 'N/A']

# FUNCTIONS


def menu():
    """This function display the menu."""
    print(" ----------------------------")
    print("│ 1 - Make your own!   $18.99│ ")
    print("│ 2 - Nachorrrito      $10.99│ ")
    print("│ 3 - Special Bowl!!!  $12.99│ ")
    print("│ 4 - Mad Salad        $9.99 │ ")
    print("│ 5 - Tacos            $8.99 │ ")
    print("│ 6 - Quesadillas      $11.99│ ")
    print(" ----------------------------")
    print()


def view_info():
    """Display the info about the restaurant."""
    print("""Tortios is a restaurant chain based in Queenstown, and was establish in 2010. Tortios is most famously known for our
Make your own order!, where customers can choose their own wrap, protein, rice, beans, and toppings. We also have a variety
of other menu items such as our Nachorrrito, Special Bowl!!!, Mad Salad, Tacos, and Quesadillas. We are open from 10am to
10pm every day of the week. We also offer delivery and pick-up options for our customers. We hope to see you soon at
Tortios!""")
    print()


def customer_program():
    """Display the different options the user could do if they had chose the customer program."""
    print("What would you like to do?")
    print("1. View menu.")
    print("2. Order.")
    print("3. View Info.")
    print("4. Exit.")


def get_number():
    """This function gets the customer's phone number, this is used for both delivery and pick-up orders, this also checks if the input is valid and if it is not, it will ask the user to input again until they input a valid phone number."""
    while True:
        phone = input("Enter Phone Number (max 10 digits): ").strip()
        if not phone.isdigit():  # checks if the input only contains digits, if it does not, it will ask the user to input again until they input a valid phone number
            print("Error: Phone number must only contain digits. Try again.")
            print()
        elif len(phone) > 10:
            print(f"Error: Number is too long ({len(phone)} digits). Max is 10. Try again")
            print()
        elif len(phone) < 7:
            print("Error: Number is too short, must be at least 7 digits. Try again.")
            print()
        else:
            return phone


def add_order():
    """Take all the details from an order."""
    print("Now, let's build your order!")
    menu()
    menu_choice = input("Enter the number of the menu item you want to order: ")
    if menu_choice == "1":
        print()
        print("--- Place Your Order ---")
        first_name = input("Enter your first name: ").title()
        last_name = input("Enter your last name: ").title()
        while True:  # the while loop is used to repeat the code until the user inputs a valid option.
            choice = input("For delivery(1) or pick-up?(2): ")
            if choice == "1":
                order_type = "Delivery"
                address = input("Enter your delivery address: ")
                break
            elif choice == "2":
                order_type = "Pick-up"
                address = None
                break
            else:                    
                print("Invalid input, Try again.")
                print()
        phone = get_number()
        while True:  # the while loop is used to repeat the code until the user inputs a valid option.
            order_choice = input("Would you like to make a custom burrito or a custom burrito bowl? (Burrito/Bowl) ").lower()
            if order_choice not in custom:
                print("Invalid input, Try again.")
                print()
            else:
                print("Alright!")
                print()
                break
        if order_choice == "burrito":
            while True:  # the while loop is used to repeat the code until the user inputs a valid option.
                custom_order = "Custom Burrito"
                wrap_choice = input("Choose a wrap (Tortilla, Veggie, Cassava): ").title()
                if wrap_choice not in wraps:
                    print("Invalid wrap choice. Please try again.")
                    print()
                else:
                    print("Alright!")
                    print()
                    break
            while True:  # the while loop is used to repeat the code until the user inputs a valid option.
                protein_choice = input("Choose a protein (Steak, Chicken, Pork, Veggie): ").title()
                if protein_choice not in proteins:
                    print("Invalid protein choice. Please try again.")
                    print()
                else:
                    print("Alright!")
                    print()
                    break
            while True:  # the while loop is used to repeat the code until the user inputs a valid option.
                rice_choice = input("Choose a rice (White, Brown, Black): ").title()
                if rice_choice not in rices:
                    print("Invalid rice choice. Please try again.")
                    print()
                else:
                    print("Alright!")
                    print()
                    break
            while True:  # the while loop is used to repeat the code until the user inputs a valid option.
                beans_choice = input("Choose a bean (Pinto, Black, Refried): ").title()
                if beans_choice not in beans:
                    print("Invalid bean choice. Please try again.")
                    print()
                else:
                    print("Alright!")
                    print()
                    break
            while True:  # the while loop is used to repeat the code until the user inputs a valid option.
                topping_choice = input("Choose a topping (Guacamole, Sour Cream, Cheese, N/A): ").title()
                if topping_choice not in toppings:
                    print("Invalid topping choice. Please try again.")
                    print()
                else:
                    print("Alright!")
                    print()
                    break

            print("Order placed successfully!")  # prints the order for the user to see after they place it
            order_id = first_name + phone
            orders[order_id] = {
            'first_name': first_name,
            'last_name': last_name,
            'order_type': order_type,
            'phone_number': phone,
            'address': address,
            'order': [custom_order, wrap_choice, protein_choice, rice_choice, beans_choice, topping_choice]
                }
            order_data = orders[order_id]

            print("\n===== ORDER RECEIPT =====")
            print(f"Name: {order_data['first_name']} {order_data['last_name']}")
            print(f"Order Type: {order_data['order_type']}")
            print(f"Phone: {order_data['phone_number']}")
            if order_type == "Delivery":
                print(f"Address: {order_data['address']}")

            print("\n--- Item Details ---")
            print(f"Item: {order_data['order'][0]}")
            print(f"Wrap: {order_data['order'][1]}")
            print(f"Protein: {order_data['order'][2]}")
            print(f"Rice: {order_data['order'][3]}")
            print(f"Beans: {order_data['order'][4]}")
            print(f"Topping: {order_data['order'][5]}")
            print("Price: $18.99")
            print("==========================")
            print()

        elif order_choice == "bowl":
            custom_order = "Custom Burrito Bowl"
            wrap_choice = "N/A"
            while True:  # the while loop is used to repeat the code until the user inputs a valid option.
                protein_choice = input("Choose a protein (Steak, Chicken, Pork, Veggie): ").title()
                if protein_choice not in proteins:
                    print("Invalid protein choice. Please try again.")                  
                    print()
                else:
                    print("Alright!")
                    print()
                    break
            while True:  # the while loop is used to repeat the code until the user inputs a valid option.
                rice_choice = input("Choose a rice (White, Brown, Black): ").title()
                if rice_choice not in rices:
                    print("Invalid rice choice. Please try again.")                
                else:
                    print("Alright!")
                    print()
                    break
            while True:  # the while loop is used to repeat the code until the user inputs a valid option.
                beans_choice = input("Choose a bean (Pinto, Black, Refried): ").title()
                if beans_choice not in beans:
                    print("Invalid bean choice. Please try again.")                    
                    print()
                else:
                    print("Alright!")
                    print()
                    break
            while True:  # the while loop is used to repeat the code until the user inputs a valid option.
                topping_choice = input("Choose a topping (Guacamole, Sour Cream, Cheese, N/A): ").title()
                if topping_choice not in toppings:
                    print("Invalid topping choice. Please try again.")               
                    print()
                else:
                    print("Alright!")
                    print()
                    break
            orders[first_name] = {'first_name' : first_name,
                                'last_name' : last_name,
                                'order_type' : order_type,
                                'phone_number' : phone,
                                'order' : [custom_order, wrap_choice, protein_choice, rice_choice, beans_choice, topping_choice]}
                
            print("Order placed successfully!")  # prints the order for the user to see after they place it
            order_id = first_name + phone
            orders[order_id] = {
            'first_name': first_name,
            'last_name': last_name,
            'order_type': order_type,
            'phone_number': phone,
            'order': [custom_order, wrap_choice, protein_choice, rice_choice, beans_choice, topping_choice]
                }
            order_data = orders[order_id]
            print("\n===== ORDER RECEIPT =====")
            print(f"Name: {order_data['first_name']} {order_data['last_name']}")
            print(f"Order Type: {order_data['order_type']}")
            print(f"Phone: {order_data['phone_number']}")
            if order_type == "Delivery":
                print(f"Address: {order_data['address']}")
            print("\n--- Item Details ---")
            print(f"Item: {order_data['order'][0]}")
            print(f"Wrap: {order_data['order'][1]}")
            print(f"Protein: {order_data['order'][2]}")
            print(f"Rice: {order_data['order'][3]}")
            print(f"Beans: {order_data['order'][4]}")
            print(f"Topping: {order_data['order'][5]}")
            print("Price: $18.99")
            print("==========================")
            print()
            
        elif menu_choice == '2':
            print()
            print("--- Place Your Order ---")
            first_name = input("Enter your first name: ").title()
            last_name = input("Enter your last name: ").title()
            while True:  # the while loop is used to repeat the code until the user inputs a valid option.
                choice = input("For delivery(1) or pick-up?(2): ")   
                if choice == "1":
                    order_type = "Delivery"
                    break
                elif choice == "2":
                    order_type = "Pick-up"
                    break
                else:
                    print("Invalid input, Try again.")
                    print()
            phone = get_number() 

            order_id = first_name + phone
            orders[order_id] = {
            'first_name': first_name,
            'last_name': last_name,
            'order_type': order_type,
            'phone_number': phone,
            'order': []
                }
            order_data = orders[order_id]
            print("\n===== ORDER RECEIPT =====")
            print(f"Name: {order_data['first_name']} {order_data['last_name']}")
            print(f"Order Type: {order_data['order_type']}")
            print(f"Phone: {order_data['phone_number']}")
            if order_type == "Delivery":
                print(f"Address: {order_data['address']}")
            print("\n--- Item Details ---")
            print("Item: Nachorrrito")
            print("Price: $10.99")
            print("==========================")
            print()

        elif menu_choice == '3':
            print()
            print("--- Place Your Order ---")
            first_name = input("Enter your first name: ").title()
            last_name = input("Enter your last name: ").title()
            while True:  # the while loop is used to repeat the code until the user inputs a valid option.
                choice = input("For delivery(1) or pick-up?(2): ")   
                if choice == "1":
                    order_type = "Delivery"
                    break
                elif choice == "2":
                    order_type = "Pick-up"
                    break
                else:
                    print("Invalid input, Try again.")
                    print()
            phone = get_number() 

            order_id = first_name + phone
            orders[order_id] = {
            'first_name': first_name,
            'last_name': last_name,
            'order_type': order_type,
            'phone_number': phone,
            'order': []
                }
            order_data = orders[order_id]
            print("\n===== ORDER RECEIPT =====")
            print(f"Name: {order_data['first_name']} {order_data['last_name']}")
            print(f"Order Type: {order_data['order_type']}")
            print(f"Phone: {order_data['phone_number']}")
            if order_type == "Delivery":
                print(f"Address: {order_data['address']}")
            print("\n--- Item Details ---")
            print("Item: Special Bowl!!!")
            print("Price: $12.99")
            print("==========================")
            print()

        elif menu_choice == '4':
            print()
            print("--- Place Your Order ---")
            first_name = input("Enter your first name: ").title()
            last_name = input("Enter your last name: ").title()
            while True:  # the while loop is used to repeat the code until the user inputs a valid option.
                choice = input("For delivery(1) or pick-up?(2): ")   
                if choice == "1":
                    order_type = "Delivery"
                    break
                elif choice == "2":
                    order_type = "Pick-up"
                    break
                else:
                    print("Invalid input, Try again.")
                    print()
            phone = get_number() 

            order_id = first_name + phone
            orders[order_id] = {
            'first_name': first_name,
            'last_name': last_name,
            'order_type': order_type,
            'phone_number': phone,
            'order': []
                }
            order_data = orders[order_id]
            print("\n===== ORDER RECEIPT =====")
            print(f"Name: {order_data['first_name']} {order_data['last_name']}")
            print(f"Order Type: {order_data['order_type']}")
            print(f"Phone: {order_data['phone_number']}")
            if order_type == "Delivery":
                print(f"Address: {order_data['address']}")
            print("\n--- Item Details ---")
            print("Item: Mad Salad")
            print("Price: $9.99")
            print("==========================")
            print()

        elif menu_choice == '5':
            print()
            print("--- Place Your Order ---")
            first_name = input("Enter your first name: ").title()
            last_name = input("Enter your last name: ").title()
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
                    print()
            phone = get_number() 

            order_id = first_name + phone
            orders[order_id] = {
            'first_name': first_name,
            'last_name': last_name,
            'order_type': order_type,
            'phone_number': phone,
            'order': []
                }
            order_data = orders[order_id]
            print("\n===== ORDER RECEIPT =====")
            print(f"Name: {order_data['first_name']} {order_data['last_name']}")
            print(f"Order Type: {order_data['order_type']}")
            print(f"Phone: {order_data['phone_number']}")
            if order_type == "Delivery":
                print(f"Address: {order_data['address']}")
            print("\n--- Item Details ---")
            print("Item: Tacos")
            print("Price: $8.99")
            print("==========================")
            print()

        elif menu_choice == '6':
            print()
            print("--- Place Your Order ---")
            first_name = input("Enter your first name: ").title()   
            last_name = input("Enter your last name: ").title()
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
                    print()
            phone = get_number() 

            order_id = first_name + phone
            orders[order_id] = {
            'first_name': first_name,
            'last_name': last_name,
            'order_type': order_type,
            'phone_number': phone,
            'order': []
                }
            order_data = orders[order_id]
            print("\n===== ORDER RECEIPT =====")
            print(f"Name: {order_data['first_name']} {order_data['last_name']}")
            print(f"Order Type: {order_data['order_type']}")
            print(f"Phone: {order_data['phone_number']}")
            if order_type == "Delivery":
                print(f"Address: {order_data['address']}")
            print("\n--- Item Details ---")
            print("Item: Quesadillas")
            print("Price: $11.99")
            print("==========================")
            print()
        else:
            print("Invalid input, Try again.")
            print("Invalid menu choice, Try again.")


# START OF THE PROGRAM



print("               -------------------------")
print("Welcome to Tortios!")
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
        print("Thank you for visiting Tortios, have a great day!")
        break
    else:
        print("Invalid input, Try again.")
        print()