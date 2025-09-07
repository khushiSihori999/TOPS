
#Write a Python function that takes two lists and returns true if they 
#have at least one common member.

def common_list(list1,list2):
    for item in list1:
        if item in list2:
            return True
        return False
    
print(common_list([1,3,5],[8,9,0]))

print(common_list([2,3,4],[2,8,0]))
        
        