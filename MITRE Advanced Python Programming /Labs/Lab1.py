#write python code that adds numvers 1 to 100

import numpy as np

# iterate through a list of numbers from 0-100 and make sure to know that
# sum of n integers formula

#my idea
for i in list(range(1, 101)):
    formula = i*(i+1)/2
    print(formula) #prints a result of all the numbers iterated through

#vid lecture idea
n =100
print(int(n*(n+1)/2))

