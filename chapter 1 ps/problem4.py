#wap to print the contests of a directory using the os module.search online for the  function which does that.
import os

directory_path = "New folder"

try:
    # Get list of files and folders
    contents = os.listdir(directory_path)

    print("\nContents of the directory:")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")

except PermissionError:
    print("You do not have permission to access this directory.")

except Exception as e:
    print("An error occurred:", e)