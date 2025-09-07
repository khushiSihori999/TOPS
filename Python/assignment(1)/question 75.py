
#Write a Python program to read last n lines of a file

# Program to read last n lines of a file

def read_last_n_lines(filename, n):
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines[-n:]:
            print(line.strip())

# Example usage
read_last_n_lines("example.txt", 3)
