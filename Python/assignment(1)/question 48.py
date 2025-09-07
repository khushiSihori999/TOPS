#Write a Python script to sort (ascending and descending) a 
#dictionary by value.


# Sample dictionary
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 5}

# Sort dictionary by value (ascending order)
asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sort dictionary by value (descending order)
desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# Print results
print("Original Dictionary:", my_dict)
print("Ascending Order:", asc_sorted)
print("Descending Order:", desc_sorted)
