
#Write a Python function to reverses a string if its length is a multiple of 4

def mul_of_4(s):
    if len(s)%4==0:
        return s[::-1]
    else:
        return s
    
print(mul_of_4("abcd"))
print(mul_of_4("fgjhjdj"))
print(mul_of_4("fgtryuie"))