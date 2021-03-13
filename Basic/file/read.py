# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file:

f = open("test.txt", "r")
print(f.read())


# If the file is located in a different location, you will have to specify the file path, like this:
#f = open("/home/aasumitro/Documents/Projects/BakodeID/JupyterNotebook", "r")


# Read Only Parts of the File
#By default the read() method returns the whole text, but you can also specify how many characters you want to return:
print(f.read(1))


# Read Lines
#You can return one line by using the readline() method:
print(f.readline())

# Close Files

f.close()