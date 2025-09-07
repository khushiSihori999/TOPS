
# Program to copy contents of one file to another

def copy_file(source, destination):
    try:
        with open(source, "r") as src:          # open source file in read mode
            content = src.read()                # read entire content
        
        with open(destination, "w") as dest:    # open destination in write mode
            dest.write(content)                 # write content to new file
        
        print("File copied successfully!")

    except Exception as e:
        print("Error while copying file:", e)


# Example usage
copy_file("exception_example.py", "destination.txt")
