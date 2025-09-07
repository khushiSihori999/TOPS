
# Write a Python function to calculate the factorial of a number (a 
# nonnegative integer)

def fact_function(n):
    if n==0 or n==1:
        return 1
    
    else:
        return n * fact_function(n-1)
    
print(fact_function(5))
    
