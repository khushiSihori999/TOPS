#Write a Python program to get a single string from two given strings, 
#separated by a space and swap the first two characters of each string.
def swap_and_combine(str1, str2):
    # If strings are at least 2 characters
    if len(str1) > 1 and len(str2) > 1:
        new_str1 = str2[:2] + str1[2:]
        new_str2 = str1[:2] + str2[2:]
    else:
        # If either string has less than 2 characters, just swap fully
        new_str1 = str2 
        new_str2 = str1 

    return new_str1 + " " + new_str2

# Example usage:
s1 = "k"
s2 = "s"
result = swap_and_combine(s1, s2)
print("Result:", result)
