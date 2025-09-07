
# differnce between append and extends

list1 = [1, 2, 3]
list1.append(4)  
print(list1)   # [1, 2, 3, 4]

list1.append([5, 6])
print(list1)   # [1, 2, 3, 4, [5, 6]]   (nested list)

list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)   # [1, 2, 3, 4, 5]

list2.extend("hi")
print(list2)   # [1, 2, 3, 4, 5, 'h', 'i']
