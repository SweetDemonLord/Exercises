# Open text file for reading
mf=open("D:\\Programming\\Python\\listings\\listings7\\poetry.txt",
        encoding="utf8")
# Reading file contents
txt=mf.read()
# Displaying file contents
print(txt)
# Close the file
mf.close()
print("The file is closed...")