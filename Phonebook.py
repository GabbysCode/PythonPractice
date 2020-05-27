whats_yo_name = input("what's ya name sugar? ")
whats_yo_numba = input("and what's yo numba'? ")


# we want to create a dictionary that when what's your name/number is called it's populated, we also want to create a
# function at one point that prints the entire phonebook, you can also create another function to see if a phone
# record exists or not, and look up via name/number! consider how you want the phonebook to be set up whether in the
# method call or via input


phonebook = {whats_yo_name: whats_yo_numba}
# print(phonebook)


def search_number():
    number_exists = input("give the name you want to find the number for ")
    print(phonebook[number_exists])

# search_number()
def search_name():
    name_exists = input("give the number you want to find the name for ")
    print(phonebook[name_exists])
    for whats_yo_name,whats_yo_numba in phonebook.items():
        if whats_yo_numba == name_exists:
            print(whats_yo_name)


search_name()

def return_names():
    print(phonebook.keys())


def return_numbers():
    print(phonebook.values())


# return_numbers()

