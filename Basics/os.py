import os

path = 'C:\\Desktop\\Python\\Basics\\assets'

if os.path.exists(path):
    print("that path exists")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("that is directory")    
else:
    print("file is not there")
