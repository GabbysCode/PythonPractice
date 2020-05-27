number = int(input("gimme a number any number "))
even = number % 2
print(even)
if even > 0:
    print("this number is odd! " + str(number))
else:
    print("this number is even! " + str(number))
