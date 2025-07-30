#Write a Python program to count occurrences of a substring in a string

main_string=input("Enter main string")

sub_string=input("Enter substring")


count = main_string.count(sub_string)

# if sub_string in main_string:
#     count+=1

print("count of frequency of substring",count)
