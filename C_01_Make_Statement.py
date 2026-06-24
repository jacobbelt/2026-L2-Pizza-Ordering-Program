# Functions go here
def make_statement(statement, deocration):
    """Empasises headings by adding decartion
    at the start and end"""

    print(f"{deocration * 3} {statement} {deocration * 3}")

# Main Routine goes here
make_statement("Programming is Fun!", "👍")