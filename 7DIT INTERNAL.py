#list of lists (lol)
password = "ilovpotle"

def staff_program():
    pass


def get_user():     #a function to check if the one handling the website is a customer or an employee/staff
    while True:
        user = input("staff or customer: ").lower()            #all of the printed statements are temporary
        if user == "customer":
            return user
        elif user == "staff":
            print("In order to access the staff thingy you need to enter a password.")      #password system
            pw_input = input("Enter the password: ")        
            if pw_input == password:
                print("Welcome!")
                return user
            else:
                print("wrong")
        else:
            print('You must input either "Customer" or "Staff", Try again.')



user = get_user()

print(user)
if user == "staff":
    staff_program()