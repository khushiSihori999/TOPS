
# Program to write a list to a file

def write_list_to_file(filename, data_list):
    with open(filename, "w") as file:   # open in write mode
        for item in data_list:
            file.write(item + "\n")   # write each item on a new line

# Example usage
my_list = ["Python", "Java", "C++", "JavaScript"]
write_list_to_file("example.txt", my_list)

print("List has been written to example.txt")

