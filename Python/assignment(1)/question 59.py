#)Write a Python program to create a dictionary from a string. 
#Note: Track the count of the letters from the string

from collections import Counter

# Sample string
my_str = "w3resource"

# Using Counter
result = dict(Counter(my_str))

print(result)
