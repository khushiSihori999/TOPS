
## Program to read a file line by line and store it into a list

def file_to_list(filename):
    with open(filename, "r") as file:
        lines = file.readlines()   # returns a list of lines
        lines = [line.strip() for line in lines]  # remove \n
    return lines

# Example usage
filename = "example.txt"
result = file_to_list(filename)
print("File stored in list:\n", result)
