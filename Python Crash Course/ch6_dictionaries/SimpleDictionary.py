#pg. 92
#simple dictionary
alien_o = {'color': 'green', 'points': 5 }

print(alien_o['color'])
print(alien_o['points'])

# dictionaries are dynamic

alien_o = {'x_position': 0, 'y_position': 25, "speed": "medium"}
#adds x,y position key pairs to alien_o
print(f"Original Position: {alien_o['x_position']}")

alien_o['speed'] = 'medium'
if alien_o['speed'] == 'slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
    print("Ah, average speed alien!")
else: #fast alien
    x_increment = 3

#now the new position of the alien
alien_o["x_position"] = alien_o["x_position"] + x_increment
print(f"New position: {alien_o['x_position']}!")

#Removing key values
#Given alien_o then we can do delete
alien_o = {'color': 'green', 'points': 5}
del alien_o['points']
print(alien_o)

# Dictionary with similar objects - pg 97

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'Edward': 'Ruby',
    'phil': 'python',
}

print(f"Sarah's favorite language is: {favorite_languages['sarah']}!")

#Using get() to access values pg 98

points = alien_o.get('color')
print(points) #returns none because points no longer exist
