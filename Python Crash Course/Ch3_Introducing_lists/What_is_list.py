# Intro

bicycles = ['trek', 'redline', 'specialized', 4]
print(bicycles)

# accessing elements on list
print(bicycles[0])  # output trek
print(bicycles[0].title())  # Trek
print(bicycles[-1])

# using vals from a list
message = f"My first bicycle was in {bicycles[0].title()}!"
print(message)

# modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)  # outputs replacement - honda to ducati

# adding/appending new element to lists
motorcycles.append('ducati')  # appends ducati to list and adds it to end
print(motorcycles)

# example

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append(4)

print(motorcycles)

# inserting elements into a list (through index)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)  # outputs ducati in index 0 (beginning) of list

# removing elements in list
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]  # removes index 0 val of list (using del statement)
print(motorcycles)

# Removing using the pop() method

## pop() let's you work with the item removed from list afterwards
motorcycles = ['honda', 4, 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() #removes last item in list by default
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 5, 'yamaha', 'suzuki']
print(motorcycles)
last_owned = motorcycles.pop()
print(f'The last motorcycle i owned was a {last_owned.title()}!')

#Removing ith item in list using pop()

motorcycles = ['honda', 6, 'yamaha', 'suzuki']
print(motorcycles)
first_owned = motorcycles.pop(0)
print(f"the first motorcycle I owned was a {first_owned.title()}")

# What about removing an item given we don't know the the position of item in list?
# We use remove() method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 7]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)
