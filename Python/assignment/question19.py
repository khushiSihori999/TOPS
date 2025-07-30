
#Write a Python program to count the occurrences of each word in a given sentence

sentence=input("Enter string")

sentence=sentence.lower()

words=sentence.split()

word_frequency={}

for word in words:
    if word in word_frequency:
        word_frequency[word]+=1
    else:
        word_frequency[word]=1

# Display the result
print("\nWord Frequency:")
for word, freq in word_frequency.items():
    print(f"'{word}': {freq}")
    
