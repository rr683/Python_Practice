# checking for special statements

#requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

#for requested_topping in requested_toppings:
#    if requested_topping == 'green peppers':
#        print("sorry we are out of that item")
#    else:
#        print(f"adding {requested_topping}.")

#print("\n finish making your pizza!")

#check that a list is not empty

#requested_toppings = []

#if requested_toppings:
#    for requested_topping in requested_toppings:
#        print(f"adding {requested_topping}")
#    print("\n finished making your pizza")
#else:
#    print("U want a plain pizza?")

#using multiple lists pg 88

available = ["mushrooms", "olives", "green peppers",
             "pepperoni", "pineapple", "extra cheese"]

requested = ["mushrooms", "french fries", "extra cheese"]

for order in requested:
    if order in available:
        print(f"adding{order}.")
    else:
        print(f"sorry, we dont have {order}")

print("\n finished making your pizza")
