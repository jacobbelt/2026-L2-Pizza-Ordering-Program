import pandas


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""
    print(f"{decoration * 3} {statement} {decoration * 3}")


def number_check(question):
    """Checks that valid integers are the right length"""
    while True:
        try:
            value = input(question).strip()
            if len(value) != 9 or not value.isdigit():
                print("Please enter a valid 9-digit phone number")
            else:
                return value
        except ValueError:
            print("Please enter a valid 9-digit phone number")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or the first n letters"""

    while True:
        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first n letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


def int_check(question, max_value=5):
    """Checks users enter an integer between 1 and max_value"""

    error = f"Please enter a valid integer between 1 and {max_value}"

    while True:
        try:
            response = int(input(question))

            if 1 <= response <= max_value:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def instructions():
    make_statement("Instructions", "ℹ️")

    print("""
Welcome to Luigi's Pizza! Here's how ordering works:

1. Enter your phone number and name.
2. Choose delivery or pickup (delivery will ask for your address).
3. View the menu if you'd like to see prices.
4. Order your pizzas:
   - Pick a pizza and how many you want.
   - You can keep adding different pizzas until you hit the 5-pizza limit.
5. Optionally add sides (chips, garlic bread, onion rings, cookies) up
   to a 5-side limit.
6. Review your final order and total cost.
7. Confirm the order is correct, or redo it if something's wrong.
 ps you can type the first letter for yes and no and with pickup and delivery eg y for yes and n for no
Let's get started!
""")


def run_order(cart, total_cost, pizzas_remaining, max_pizzas):
    """Runs the pizza ordering loop and returns updated cart, total, and pizzas remaining"""

    while pizzas_remaining > 0:

        print()
        pizza_choice = string_check(
            "What pizza would you like? ",
            menu
        )
        print(f"You have {pizzas_remaining} pizza(s) left that you can order")
        amount = int_check(
            f"How many {pizza_choice} pizzas would you like? ",
            pizzas_remaining
        )

        cost = price_dict[pizza_choice] * amount
        total_cost += cost
        pizzas_remaining -= amount

        cart.append([pizza_choice, amount, cost])

        print(
            f"You ordered {amount} {pizza_choice} pizza(s) "
            f"for ${cost}"
        )

        if pizzas_remaining == 0:
            print(f"\nYou've reached the {max_pizzas} pizza limit.")
            break

        more_pizza = string_check(
            "Would you like to order another pizza? "
        )

        if more_pizza == "no":
            break

    return cart, total_cost, pizzas_remaining


def run_sides(sides_cart, total_cost, sides_remaining, max_sides):
    """Runs the sides ordering loop and returns updated sides cart, total cost, and sides remaining"""

    want_sides = string_check(
        "Would you like to add any sides to your order? "
    )

    if want_sides == "no":
        return sides_cart, total_cost, sides_remaining

    print()
    print(sides_frame)

    while sides_remaining > 0:
        print()
        print(f"You have {sides_remaining} side(s) left that you can order")
        side_choice = string_check(
            "Which side would you like? ",
            sides
        )
        amount = int_check(
            f"How many {side_choice} would you like? ",
            sides_remaining
        )

        cost = price_sides_dict[side_choice] * amount
        total_cost += cost
        sides_remaining -= amount

        sides_cart.append([side_choice, amount, cost])

        print(
            f"You ordered {amount} {side_choice} "
            f"for ${cost}"
        )

        if sides_remaining == 0:
            print(f"\nYou've reached the {max_sides} side limit.")
            break

        more_sides = string_check(
            "Would you like to add another side? "
        )

        if more_sides == "no":
            break

    return sides_cart, total_cost, sides_remaining

# Menu data
menu = [
    'cheese',
    'pepperoni',
    'meat-lovers',
    'veggie',
    'white',
    'cheesy garlic',
    'ham and cheese',
    'hawaiian',
    'buffalo chicken',
    'beef and onion'
]

price = [5, 7, 12, 7, 8, 6, 8, 9, 13, 9]

pizza_menu_dict = {
    "Pizza": menu,
    "Price ($)": price
}
order_type = ["delivery", "pickup"]
menu_frame = pandas.DataFrame(pizza_menu_dict)
menu_frame.index = menu_frame.index + 1

# Create a dictionary for easy price lookup
price_dict = dict(zip(menu, price))


sides = [
    'chips',
    'garlic bread',
    'onion rings',
    'cookies',
]
price_sides = [3, 5, 4, 2]

sides_menu_dict = {
    "Side": sides,
    "Price ($)": price_sides
}
sides_frame = pandas.DataFrame(sides_menu_dict)
sides_frame.index = sides_frame.index + 1

# Create a dictionary for easy price lookup
price_sides_dict = dict(zip(sides, price_sides))


# Main routine
make_statement("Luigi's Pizza", "🍕")

while True:
    print()
    want_instructions = string_check(
        "Do you want to see the instructions? "
    )

    if want_instructions == "yes":
        instructions()

    phone_number = number_check("What is your phone number? ")
    name = not_blank("What is your name? ")

    delivery_pickup = string_check("Would you like to do delivery or pickup? ", order_type)
    if delivery_pickup == "delivery":
        while True:
            address = input("Please enter your address ")

            if address.strip() != "":
                break
            print("Invalid address. Please try again.")
        print(f"Your address is {address}")
        print(f"Your phone number is {phone_number}")
        print(f"Your name is {name}")
    if delivery_pickup == "pickup":
        print(f"Your phone number is {phone_number}")
        print("You picked pickup")
        print(f"Your name is {name}")

    print()
    read_menu = string_check(
        "Would you like to see the menu? "
    )

    if read_menu == "yes":
        print()
        print(menu_frame)

    # Cart stores all orders
    cart = []
    sides_cart = []
    total_cost = 0
    MAX_PIZZAS = 5
    MAX_SIDES = 5
    pizzas_remaining = MAX_PIZZAS
    sides_remaining = MAX_SIDES

    print(f"\nYou can order a maximum of {MAX_PIZZAS} pizzas in total.")

    cart, total_cost, pizzas_remaining = run_order(cart, total_cost, pizzas_remaining, MAX_PIZZAS)

    print()
    sides_cart, total_cost, sides_remaining = run_sides(sides_cart, total_cost, sides_remaining, MAX_SIDES)

    # Print final order
    make_statement(F"{name}'s order", "🛒")

    for pizza, amount, cost in cart:
        print(f"{amount} x {pizza} pizza = ${cost}")

    for side, amount, cost in sides_cart:
        print(f"{amount} x {side} = ${cost}")

    print(f"Your phone number is {phone_number}")
    if delivery_pickup == "delivery":
        print(f"Your address is {address}")
    if delivery_pickup == "pickup":
        print(f"Your name is {name}")
    print(f"Total Cost: ${total_cost}")

    correct_order = string_check("Is this your correct order? ")

    if correct_order == "no":
        # correct_order == "no" -> ask if they want to redo the order
        redo = string_check("Do you want to redo your order? ")
        if redo == "no":
            # They don't want the order they built, and don't want to redo it,
            # so treat it as cancelled and end the program.
            make_statement("Thank you for ordering at Luigi's!", "🍕")
            break

        continue

    add_more = string_check("Do you want to place another order? ")
    if add_more == "no":
        make_statement("Thank you for ordering at Luigi's!", "🍕")
        break