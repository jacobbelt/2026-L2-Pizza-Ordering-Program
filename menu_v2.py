import pandas
# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from a range of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")
# Functions go here
def int_check(question ):
    """ Checks users enter an integer bet"""

    error = f"We only allow an order of 1 to 5 pizzas"

    while True:
        try:
            response = int(input(question))

            if 1 <= response <= 5:
                return response
            else:
                print(error)

        except ValueError:
            print(error)






def instructions():
    make_statement("Instructions", "ℹ️")

    print('''

I LOVE MAKING OUT WITH PIZZA

    ''')

menu = ['cheese','pepperoni','meat-lovers','veggie','white','cheesy garlic','ham and cheese', 'hawaiian', 'buffalo chicken','beef and onoin']
price = [5,5,5,5,5,5,5,5,10,13]

pizza_menu_dict = {
    "Pizza's": menu,
    'price': price
}

menu_frame = pandas.DataFrame(pizza_menu_dict)


# Main routine goes here

make_statement("Luigi's pizza", "🍕")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
read_me = string_check("Would you like to see the menu? ")
if read_me == "yes":
    print(menu_frame)

pizza_choice = string_check("What pizza would you like? ", menu)

amount = int_check(f"How many {pizza_choice} pizzas would you like? ")

print(f"You ordered {amount} {pizza_choice} pizza")
more_pizza = string_check("Would you like to order another pizza? ")

if more_pizza == "yes":
        pizza_choice = string_check("What pizza would you like? ", menu)

        amount = int_check(f"How many {pizza_choice} pizzas would you like? ")
        more_pizza = string_check("Would you like to order another pizza? ")
if more_pizza == "no":
    cart = pizza_choice
    print(cart)
