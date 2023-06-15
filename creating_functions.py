def get_message():
    return "Hello world"

a = get_message
b = get_message()
print(f"b: {b}")
print(get_message())

def show_message():
    message = get_message()
    print(message)

show_message()

def hello(target):
    print(f"Hello, {target}")

hello("Mom")
hello("New York")
hello("world")

def multihello(greeting: str, *targets: str) -> None:
    for target in targets:
        print(f"{greeting}, {target}")

multihello("Hi", 'John')
multihello("Hey", 'John', 'Paul', 'George', 'Ringo')
multihello("Howdy")
multihello(5, 99)


def to_letters(s):
    return list(s)

name = "Francis"
print(to_letters(name))

def doit():
    print("blah blah blah")

x = doit()
print(f"x: {x}")

doit()

animal = "wombat"  # GLOBAL variable  (global to current file)

def spam():
    country  = "Burkina Faso"  # LOCAL variable
    print(f"animal: {animal}")
    
spam()
# print(f"country: {country}")


















