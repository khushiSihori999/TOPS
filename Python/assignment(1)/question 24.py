
#Write a Python function to insert a string in the middle of a string

def insert_middle(original,insert):

    mid=len(original)//2

    return original[:mid] + insert + original[mid:]

print(insert_middle("hello","wold"))
    