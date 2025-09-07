
#Write a Python program to read first n lines of a file.

# Program to read first n lines of a file

def read_first_n_lines(filename, n):
    with open(filename, "r") as file:
        for i in range(n):
            line = file.readline()
            if not line:   # Stop if file has fewer than n lines
                break
            print(line.strip())

# Example usage
filename = "example.txt"
n = 3  # number of lines to read
read_first_n_lines(filename, n)
