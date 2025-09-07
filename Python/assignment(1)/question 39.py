
#Write a Python program to find the second smallest number in a list.

def second_smallest(lst):
    numbers=list(set(lst))

    numbers.sort()
    if len(numbers)<2:
        return None
    else:
        return numbers[1]
    

num=[3,5,6,3,7,8]
print("smallest second",second_smallest(num))