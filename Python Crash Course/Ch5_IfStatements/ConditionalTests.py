# Conditional test pg 72

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Checking for inequality
requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print("Hold the anchovies")

answer = 17
if answer != 42:
    print("this is not the correct answer. Try again!")

# Checking whether value is in a list
#request_toppings = ['mushrooms', 'onions', 'pineaple']
#'mushrooms' in request_toppings #output = True

# Checking whether valie is not in a list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")