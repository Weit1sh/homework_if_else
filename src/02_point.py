print("Enter x")
x = int(input(">>> "))

print("Enter y")
y = int(input(">>> "))

if x > 0 and y > 0:
    print("This point is in 1 quarter.")
elif x < 0 and y > 0:
    print("This point is in 2 quarter.")
elif x < 0 and y < 0:
    print("This point is in 3 quarter.")
elif x > 0 and y < 0:
    print("This point is in 4 quarter.")
else:
    print("This point is inside all quarters")
