

#Write a Python program to select an item randomly from a list

import random
def pick_random(lst):

    return random.choice(lst)

items=[10,20,40,50]
print("random",pick_random(items))