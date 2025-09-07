


#Write a Python program to check a list is empty or not

def check_empty(lst):
    if not lst:   # empty list is treated as False
        print("The list is empty")
    else:
        print("The list is not empty")

# Example usage:
list1 = []
list2 = [10, 20, 30]

check_empty(list1)  # The list is empty
check_empty(list2)  # The list is not empty
