
#Write a Python function that takes a list and returns a new list with 
#unique elements of the first list.

def unique_list(list):
    unique=[]

    for item in list:
        if item not in unique:
            unique.append(item)

    return unique

print(unique_list([2,2,4,5,6,6]))        