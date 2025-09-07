
#Write a Python program to read an entire text file.

# Program to read an entire text file

# Open file in read mode
file = open("function_example1.py", "r")

# Read the entire content
content = file.read()

# Print content
print("📄 File Content:\n")
print(content)

# Close the file
file.close()
