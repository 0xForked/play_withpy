import os

if os.path.exists("test3.txt"):
    os.remove("test3.txt")
else:
    print("The file does not exist")
