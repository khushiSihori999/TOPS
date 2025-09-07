

# Write a Python program to count the number of strings where the string 
# length is 2 or more and the first and last character are same from a given list 
# of strings.


def count_word(words):
    count=0
    for word in words:
        if len(word)>=2 and word[0]==word[-1]:
            count+=1
    return count
    
word_list=['abc','xyz','aba','1221','aa','x']

print("count of words",count_word(word_list))