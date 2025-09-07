#Write a Python function to check whether a number is in a given range

def num_in_range(num,start,end):
    if num in range(start,end+1):
        return True
    else:
        return False
    
print(num_in_range(5,6,10))
    