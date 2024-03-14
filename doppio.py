def drink(coffee):
    print(f"I like to drink {coffee}")


def future(ideas):
    print(f"I would like a {ideas}")


def food(food_type):
    print(f"I like to eat {food_type}")


def affinity():
    drink("coffee")
    food("sushi")


if __name__ == "__affinity__":
    affinity()
# __name__ is a special variable that is set by python to be "main"
# when you call a file in the terminal
# When you are importing a file, and not running directly under the command line, 'Main' will not get called.


