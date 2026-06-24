# Functions go here
def int_check(question):
    """ Checks users enter an integer bet"""

    error = f"Oops - please enter an in integer."

    while True:
        try:
            response = int(input(question))


            return response


        except ValueError:
            print(error)


while True:

    print()



    name = input("Name: ")

    age = int_check("Age: ")

    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")