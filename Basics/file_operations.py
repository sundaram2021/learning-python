
# reading files
# try:
#     with open("./assets/text.txt") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("file not found")        

# print(file.closed)

# writing files
# text = "Hello, We are performing writing operations in file"
# with open('./assets/text.txt', "w") as file:
#     file.write(text)


# appending in files
# text = "\nSee ya!!"
# with open('./assets/text.txt', "a") as file:
#     file.write(text)


# copying files using shutil module
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata(file's creation and modifications times)


# import shutil

# # shutil.copyfile('./assets/text.txt', "./assets/text1.txt") # src, dst
# shutil.copy2('./assets/text.txt', "./assets/text2.txt")



# ----------------------------------------------------
# Moving file
# import os

# source = "./assets/text.txt"
# destination = "./assets/text4.txt"

# try: 
#     if os.path.exists(destination):
#       print("File is already created")
#     else:
#         os.replace(source, destination)
#         print(source + " was moved")
# except FileNotFoundError:
#     print("File not found")   


#--------------------------------------------------------
# Delelting files

import os

path = './assets/text4.txt'
path2 = 'empty_folder'

try: 
    # os.remove(path)
    os.rmdir(path2)  # to delete empty folder
except PermissionError:
    print("You cannot delete that file")
except FileNotFoundError:
    print("file not found")    
else:
    print(path + " was deleted")
