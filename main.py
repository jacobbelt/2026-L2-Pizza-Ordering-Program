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


def instructions():
    make_statement("Instructions", "ℹ️")

    print('''

I LOVE MAKING OUT WITH PIZZA

    ''')

menu = ['cheese','pepperoni','meat-lovers','veggie','white','cheesy garlic','ham and cheese', 'hawaiian', 'buffalo chicken','beef and onoin']
# Main routine goes here

make_statement("Luigi's pizza", "🍕")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()
read_menu = string_check("Would you like to see the menu ? ")

if read_menu == "yes":
    print("cheese pizza ")
    print("pepperoni pizza")
    print("meat-lovers pizza")
    print("veggie pizza")
    print("white pizza")
    print("cheesy garlic pizza")
    print("ham and cheese")
    print("hawaiian pizza pizza")
    print("buffalo chicken pizza")
    print("beef and onion pizza")
item1 = string_check("what pizza would you like? ",   menu)
(f"How many {item1} pizzas do you want? ")