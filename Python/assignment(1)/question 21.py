
# #Write a Python program to add 'in' at the end of a given string (length 
# should be at least 3). If the given string already ends with 'ing' then 
# add 'ly' instead if the string length of the given string is less than 3, 
# leave it unchanged.

def add_suffix(word):
    if len(word)<3:
        return word
    elif word.endswith("ing"):
        return word+"ly"
    else:
        return word+"ing"
    
print(add_suffix("play"))
print(add_suffix("playing"))
print(add_suffix("go"))