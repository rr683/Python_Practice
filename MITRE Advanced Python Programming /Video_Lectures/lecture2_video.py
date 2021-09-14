# string class

# immutable -- cannot change them

s = 'Rollo Tomasi' #single qoutes

s = 'hello' 'world'
print(s) #hellow world

s = 'Don\'t stop believing'
print(s)

s= "\"To be or not to be\""
print(s)

s = """
This is a multiline 
string 
"""
print(s)

#All s print the messages back to back

z = 3*"Da"
print(z)

z = 'abcdefg'
print(z[-1]) #accessing the string and returning last character
print(z[len(z) - 1]) #returning last character

#slicing

print(z[0:3]) #abc
print(z[-2:]) #start from second to last and print the remaining characters

# s[0] = "x" <- this will be an error; string is immutabel
new_z = "x" + z[1:]
print(new_z)



