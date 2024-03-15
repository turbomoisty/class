def drink(coffee):
    print(f"I like to drink {coffee}")


def future(ideas):
    print(f"I would like a {ideas}")


def food(food_type):
    print(f"I like to eat {food_type}")


def affinity():
    drink("coffee")
    food("sushi")


import blanku



def check_squared():
    assert blanku.squared(2) == 4
    assert blanku.squared(3) == 10


if __name__ == "__main__":
    check_squared()
# __name__ is a special variable that is set by python to be "main"
# when you call a file in the terminal
# When you are importing a file, and not running directly under the command line, 'Main' will not get called.
