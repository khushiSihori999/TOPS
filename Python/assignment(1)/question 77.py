
## Program to read a file line by line and store it into a variable

def file_to_variable(filename):
    content = ""
    with open(filename, "r") as file:
        for line in file:
            content += line   # add each line to variable
    return content

# Example usage
filename = "example.txt"
data = file_to_variable(filename)
print("File stored in variable:\n")
print(data)
