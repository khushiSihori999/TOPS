
#What is List? How will you reverse a list?
numbers = [1, 2, 3, 4, 5]
reversed_list = list(reversed(numbers))
print(reversed_list)   # [5, 4, 3, 2, 1]


numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print(reversed_list)   # [5, 4, 3, 2, 1]

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)   # [5, 4, 3, 2, 1]
