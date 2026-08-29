# Challenge 3 — File error
# Create:
# def read_file(file_path):
#     ...
# It should:
# read a file
# return its contents
# handle FileNotFoundError
# Test it with:
# an existing file
# a file that doesn't exist
def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return None
file_content = read_file("notes.txt")
print(file_content)