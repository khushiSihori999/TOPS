
#Write a Python program to append text to a file and display the text.

# Program to append text to a file and display it

# Step 1: Append text to the file
with open("example.txt", "a") as file:
    file.write("\nThis line is newly appended to the file.")

# Step 2: Read and display updated content
with open("example.txt", "r") as file:
    content = file.read()
    print("📄 Updated File Content:\n")
    print(content)
