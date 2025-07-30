

# swap without temp variable
a=10
b=20

print("before swap")
print("a=",a,"b=",b)

a=a+b
b=a-b
a=a-b


print("after swap")
print("a=",a,"b=",b)
