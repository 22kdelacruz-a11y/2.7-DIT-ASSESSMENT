#list of lists (lol)
password = "pw"
orders = []


#functions
def menu():
    print("1 - Make your own!")
    print("2 - Nachorrrito")
    print("3 - Special Bowl!!!")
    print("4")

def customer_program():
    print("What would you like to do?")
    print("1. View menu.")
    print("2. Order.")
    print("3. Exit.")

def owner_program():
    print("What would you like to do?")
    print("1. View orders.")
    print("2. Cancel orders")
    print("3. Exit.")

def get_user():  #a function to check if the one handling the website is a customer or an employee/staff
    print()
    print("               -------------------------")
    print("Welcome to n/a! Are you the owner or a customer?")
    while True:
        user = input(": ").lower()   #all of the printed statements are temporary
        if user == "customer":
            return user
        elif user == "owner":
            print()
            print("In order to access the owners account, you would need to enter a password. To return, input X.")      #password system
            pw_input = input("Enter the password: ").lower()     
            if pw_input == password:
                print()
                print("               -------------------------")
                print("Welcome!")
                return user
            if pw_input == "x":
                print()
                print("               -------------------------")
                print("Welcome to n/a! Are you  the owner or a customer?")
                continue
            else:
                print()
                print("Incorrect password. Try again.")
                
        else:
            print()
            print('You must input either "Customer" or "Owner", Try again.')
            



user = get_user()

if user == "owner":
    owner_program()
owner_input = int(input(": "))

if user == "customer":
    customer_program()
    


