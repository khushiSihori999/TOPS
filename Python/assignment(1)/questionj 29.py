
#Write a Python function to get the largest number, smallest num 
#and sum of all from a list.

def max_min_sum(nums):
    max1=max(num)
    min1=min(num)
    sum1=sum(num)

    return max1,min1,sum1

num=[6,89,3,6]

largest,smallest,total =max_min_sum(num)

print("largest",largest)
print("smallest",smallest)
print("total",total)
