
#Write a Python program to get unique values from a list
def unique_values(lst):
    return list(set(lst))

# Example usage:
nums = [1, 2, 2, 3, 4, 4, 5, 1]
print("Unique values:", unique_values(nums))
