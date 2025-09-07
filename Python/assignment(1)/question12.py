
# Write a Python program to sum of three given integers. However, if
#two values are equal sum will be zero. 

def custom_sum(a,b,c):
    if a==b or b==c or c==a:
        return 0
    else:
        return a+b+c
    
x=int(input("enter first number"))
y=int(input("Enter second number"))
z=int(input("enter ythird number"))

result=custom_sum(x,y,z)
print(result)