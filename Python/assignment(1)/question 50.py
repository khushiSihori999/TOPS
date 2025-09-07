# Write a Python script to check if a given key already exists in a 
# dictionary


# Sample dictionary
my_dict = {1: 'Apple', 2: 'Banana', 3: 'Cherry'}

# Key to check
key_to_check = 2

# Method 1: Using 'in'
if key_to_check in my_dict:
    print(f"Key {key_to_check} exists in the dictionary.")
else:
    print(f"Key {key_to_check} does not exist in the dictionary.")

# Method 2: Using .keys()
if key_to_check in my_dict.keys():
    print(f"(Using .keys()) Key {key_to_check} exists in the dictionary.")
