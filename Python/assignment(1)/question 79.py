
## Program to count number of lines in a file

def count_lines(filename):
    with open(filename, "r") as file:
        line_count = sum(1 for line in file)  # counts each line
    return line_count

# Example usage
filename = "example.txt"
print("Number of lines in file:", count_lines(filename))
