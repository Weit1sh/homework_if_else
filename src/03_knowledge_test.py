import random
print("Enter the operation")
op = input(">>> ")

x = random.randint(10, 99)
y = random.randint(10, 99)
u = random.randint(1, 9)
j = random.randint(1, 9)
pl = x + y
mn = x - y
qwerty = u * j

if op == "+":
    print("Enter the answer " +  str(x) + " + " + str(y))
    q = int(input(">>> "))
    if q == pl:
        print("You're right!")
    else: 
        print("Your answer is incorrect.")
elif op == "-":
    print("Enter the answer " +  str(x) + " - " + str(y) )
    h = int(input(">>> "))
    if h == mn:
        print("You're right!")
    else: 
        print("Your answer is incorrect.")
elif op == "*":
    print("Enter the answer " +  str(u) + " * " + str(j))
    y = int(input(">>> "))
    if y == qwerty:
        print("You're right!")
    else: 
        print("Your answer is incorrect.")
else:
    print("Sorry, but unfortunately there is no such operation.")