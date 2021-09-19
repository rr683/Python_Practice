# Looping through entire lists

##Page 50##
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'\n{magician}, that was a great trick!\n')

print('Thank you everyone')

# Numerical lists
for value in range(1, 5):
    print(value)

even_numbers = list(range(2,11,2))
print(even_numbers)

# Making a list of square numbers
squares = []
for value in range(1,11): #for every value in list
    sq_val = value**2 #square values and store that in sq_val
    squares.append(sq_val) #add that list to square list

print(squares)

# Alternative way to code above for-loop squares vals
squares = [value**2 for value in range(1, 12)]
print(squares)

#copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]
print(my_foods)
my_foods.append('cannoli')
friend_food.append('ice cream')
#both my_foods and friend_food are different lists now
print([my_foods, friend_food])