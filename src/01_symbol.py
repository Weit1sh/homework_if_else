print("Enter the x:")
x = input(">>> ")
if x.isnumeric():
    print("X = number!")
elif x.isalpha() and x.islower():
    print("X = small letter!")
elif x.isalpha() and x.isupper():
    print("X = big letter!")
else:
    print("X = symbol!")