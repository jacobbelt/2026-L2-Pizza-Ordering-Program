# Functions go here
def num_check(question, num_type, exit_code=None):
    """ Checks users enter an integer / float that is more than
    zero (or the optional exit code)"""
    if num_type == "integer":
        error = "Oops - please enter and integer more then zero."
        change_to = int
    else:
        error = "Oops - please enter and integer more then zero."
        change_to = float


    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


while True:
    print()

    my_float = num_check("Please enter a number more then 0: ", "float")
    print(f"Thanks. You chose {my_float}")
    my_int = num_check("Please enter an integer more then 0: ",
                       "integer", "")
    if my_int == "":
        print("you have chosen infinite mode ")
    else:
        print(f"Thanks. You chose {my_int}")