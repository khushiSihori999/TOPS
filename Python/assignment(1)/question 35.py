
#Write a Python program to generate and print a list of first and last 5 
#elements where the values are square of numbers between 1 and 30.

def square2():
    squares1=[x**2 for x in range(1,31)]

    print("squares of first 5 element", squares1[:5])

    print("last  5 elements:", squares1[-5:])

square2()


# def squares_list():
#     # Generate list of squares from 1 to 30
#     squares = [x**2 for x in range(1, 31)]
    
#     # Print first 5 and last 5 elements
#     print("First 5 elements:", squares[:5])
#     print("Last 5 elements:", squares[-5:])

# # Example usage
# squares_list()
