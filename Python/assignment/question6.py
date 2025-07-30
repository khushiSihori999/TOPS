
n=int(input("Enter nth term for fibonacci sereies"))

a,b=0,1
count=0

if n<=0:
    print("Enter positive integer")
elif n==1:
    print("Fibonacci sequence")
    print(a)
else:
    print("Fibonacci sequence:")
    while count<n:
        print(a, end=" ")
        c=a+b
        a=b
        b=c
        count+=1
