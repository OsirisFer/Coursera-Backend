# File handling module, it can be in text format or binary format, difference is in the way data is stored
# open fuction to open a file
# close is the other handling function to close the file after use
# Mode 'r' is for reading, 'r+' is for reading and writing, 'rb' is for reading in binary mode  
file = open("example.txt", mode="r")
data = file.readline()  # reads a single line from the file
print(data)
file.close()  # closing the file after use

with open("newfile.txt", mode="r") as file: # using 'with' automatically closes the file after the block
    print(file.read(23))  # reads first 23 characters from the file OR
    print(file.readlines())  # reads all lines and returns a list of lines  OR 
    data = file.readline()  # reads a single line from the file 
    for x in data :  # iterating through each character in the line
        print(x)


with open("newfile.txt", mode="w") as file: # 'w' mode to write to a file, creates a new file or overwrites existing
    file.write("Hello, World!\n")  # con w lo sobreescribe, para editar uso append 'a'
    file.writelines(["Hola"])  # a diferencia de write, writelines escribe una lista de lineas

#si uso la letra a en vez de w, agrega al final del archivo sin borrar lo que ya habia
with open("newfile.txt", mode="a") as file: 
    file.write("Appending a new line.\n")