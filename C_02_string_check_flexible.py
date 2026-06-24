# Functions go here
def string_check(question, valid_ans_list=('yes','no'),
                 num_letters=1):
    """ Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            if response == item:
                return item

            # check if it's the first letter
            elif response == item[num_letters]:
                return item

        print(f"Please choice an option from {valid_ans_list}")

# Main routine goes here


while True:
    want_instructions = string_check("Do you want to see the instructions? ")
    print(f"You chose {want_instructions}")
    print()
