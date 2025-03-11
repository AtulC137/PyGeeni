import os

def print_directory_structure(path):
    for dirpath, dirnames, filenames in os.walk(path):
        print(dirpath)
        for dirname in dirnames:
            print("  ", dirname)
        for filename in filenames:
            print("  ", filename)

# Call the function with the root directory of your Django project
print_directory_structure("chats") 