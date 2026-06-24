# Functions go here
def int_check(question, low, high):
    """ Checks users enter an integer bet"""

    error = f"Oops - please enter an in integer between {low} and {high}"

    while True:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


while True:

    print()

    my_num = int_check("Choose a number: ", 1, 10)
    print(f"The first number you chose is: {my_num}")

    my_num = int_check("Choose another number: ", 5, 20)
    print(f"The second number you chose is: {my_num}")