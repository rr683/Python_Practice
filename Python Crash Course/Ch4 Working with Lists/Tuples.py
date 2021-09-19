#page 65: Tuples

dimensions = (200, 50)
print(dimensions[0], dimensions[1], "first exercise")
#Immutable/vals can't be changed inside the list-- if we try dimension[0] = 250: then error will be returned

# Looping through vals of tuples
#my idea: this way you can print out however many index/vals you want from any list (you control the range)
for dimension in range(0, len(dimensions) - 1):
    print(dimensions[dimension], "The way i thought about looping a tuple")

#book's style
for dimension in dimensions: #lisy all dim in dimensions - can't change what you output
    print(dimension, "books way of looping through tuple")


