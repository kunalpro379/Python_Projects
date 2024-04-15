def create_file(file_name):
    try:
        with open(file_name,'w') as f:
            f.write("Initial content in the file.\n")
        print("File created successfully:", file_name)
    except Exception as e:
        print('an error occurred' ,e)
def append_to_file(file_name, data):
    try:
        with open(file_name, 'a') as f:
            f.write(data)
        print("Data appended to the file successfully.")
    except Exception as e:
        print("An error occurred while appending to the file:", e)

def display_file(file_name):
    try:
        with open(file_name, 'r') as f:
            print("Content of the file:")
            print(f.read())
    except Exception as e:
        print("An error occurred while reading the file:", e)
def count_file_stats(file_name):
    lines = 0
    words = 0
    characters = 0
    with open(file_name, 'r') as f:
        for line in f:
            lines += 1
            words += len(line.split())
            characters += len(line)

    return lines, words, characters

import os
def display_files_in_directory():
    current_dir=os.getcwd()
    files=os.listdir(current_dir)
    print("files available in the current dir")
    for file in files:
        print(file)
display_files_in_directory()
# Create a file
file_name = "example.txt"
create_file(file_name)

# Append data to the file
data_to_append = 'hello motherfucker\n'
append_to_file(file_name, data_to_append)

# Display the entire file
display_file(file_name)
lines, words, characters = count_file_stats(file_name)
print("Number of lines:", lines)
print("Number of words:", words)
print("Number of characters:", characters)