name = input("Enter a name, please: ")

def two_fer(name):
    if not name:
        name = "you"
    print("One for " + name + ", one for me.")

two_fer(name)

