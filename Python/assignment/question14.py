

#Write a python program to sum of the first n positive integers.#

num=int(input("enter positive interger number"))

if num<=0:
    print("enter positive interger number")
else:
    total=0
    for i in range(1,num+1):
        total+=i
    print(total)

