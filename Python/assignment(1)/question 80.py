## Program to count frequency of words in a file

def word_frequency(filename):
    with open(filename, "r") as file:
        text = file.read().lower()        # read all content and convert to lowercase
        words = text.split()              # split text into words
        freq = {}                         # dictionary to store word counts

        for word in words:
            word = word.strip(".,!?;:()[]{}\"'")  # remove punctuation
            if word:
                freq[word] = freq.get(word, 0) + 1

    return freq

# Example usage
filename = "example.txt"
result = word_frequency(filename)

print("Word Frequency in file:\n")
for word, count in result.items():
    print(f"{word} : {count}")
