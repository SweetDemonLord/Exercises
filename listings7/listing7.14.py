print("File copying starts")
# Controlled code
try:
    # A binary file is opened for reading
    A=open("C:\\Users\\Insaf\\Pictures\\samir.jpg","rb")
    # Create a binary file
    B=open("D:\\Programming\\ya.jpg","xb")
    # Contents of the first file is read
    # and written to the second file
    B.write(A.read())
    # The files are closed
    A.close()
    B.close()
    print("File copying ends")
# If the second is already existed
except FileExistsError:
    print("Error: Such file already exists")
# All others errors
except:
    print("Error: File access")
print("The program ends")

