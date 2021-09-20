#Simple if-statements

age = 17
if age >= 18.1:
    print("Alright you are old enough")
    print("Have you registered")
else:
    print("sorry you are too young")
    print("come back when you are 18")

# The elif
age = 12
if age < 2:
    print("Your admission is for free")
elif age < 18:
    print("Your admission is 10 bucks")
else:
    print("Your admission cost is 20")

# alternative
age = 35
if age < 4:
    price = 0
elif age < 20:
    price = 25
else:
    price = 40

print(f"your admission tix is {price}")

# toppings-- multiple conditions
requested_toppings = ['mushrooms','beef', 'extra cheese']
if 'mushrooms' or "beef" in requested_toppings:
    print("Adding mushrooms and beef")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'extra cheese':
    print("adding extra cheese")

print("\n Finished making your pizza")

