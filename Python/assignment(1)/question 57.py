
#question 57

#Write a Python program to find the highest 3 values in a dictionary

my_dict={'black':50,'green':80,'red':30,'pink':21}

highest_sorted=sorted(my_dict.values(),reverse=True)[:3]

print(highest_sorted)
