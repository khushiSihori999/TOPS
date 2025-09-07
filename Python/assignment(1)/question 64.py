
#Write a Python function that checks whether a passed string is 
#palindrome or not

def is_palindrom(s):
    return s==s[::-1]

print("hello is palindrom",is_palindrom("hello"))

print("madam is palindrom",is_palindrom("madam"))


