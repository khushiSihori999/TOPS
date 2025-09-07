

# Get input from user
n = int(input("Enter the number of terms in Fibonacci series: "))

# First two terms
a, b = 0, 1
count = 0

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence upto 1 term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        count += 1
