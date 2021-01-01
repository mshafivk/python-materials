def read_name():
    return input("Enter your name: ")
name=read_name()
is_valid_name = 3 <= len(name) <= 50

while not is_valid_name:
    if len(name) < 3:
        print("Name must be at least 3 characters long")
        name=read_name()
        is_valid_name = 3 <= len(name) <= 50
    elif len(name) > 50:
        print("Maximum allowed length is 50 characters.. Sorry!")
        name = read_name()
        is_valid_name = 3 <= len(name) <= 50
print(f"Name you entered is: {name}")
