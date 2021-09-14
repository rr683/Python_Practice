## Organizing a list

## Page 42 ##
# Using the sort() method

cars = ['bmw', 'audi', 'toyota', 'subaru']
#sorts list permanently
cars.sort()
print(cars)

# Sorting in reverse by setting reverse = True inside method
cars = ['bmw', 'audi', 'toyota', 'subaru', 'xy1']
cars.sort(reverse=True)
print(cars)

# Using sorted() method and change list temporarily
cars = ['bmw', 'audi', 'toyota', 'subaru', 'xy2']
print("Here is original list")
print(cars)

print("\n here is sorted list ")
print(sorted(cars))

print("\n here is original")
print(cars)

# Using reverse() method
cars = ['bmw', 'audi', 'toyota', 'subaru', 'xy3']
cars.reverse()
print(cars)


