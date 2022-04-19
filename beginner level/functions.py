# simple function

def greet():
    print("Hello Dhayo")
    print("How're you doing Rose?")
    print("How's the weather?")

# greet()

# function that allows input

def greet_name(name):
    print(f"\nHello {name}")
    print(f"How're you doing {name}")

# greet_name("Dhayo")

# Function with more than one inputs
def greet_with(name, location, other_name):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    print(f"and I know you like {other_name}")

greet_with("Zendaya", "New York", "Tom Holland")
