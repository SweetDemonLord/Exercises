# Text literal without prefix
A="\"Java\"n\"Python\""
print(A)
print("Symbols:", len(A))
# Text literal with prefix
B=r"\"Java\"\n\"Python\""
print(B)
print("Symbols:", len(B))
name="Python"
# Variable with text value
C=f"{name} language - simple and clear"
print(C)
C=f"{name!r} language - simple and clear"
# Variable with number value
num=12.34567
txt=f"Number: {num:9.3f}"
print(txt)
txt=f"Number: {num:09.3f}"
print(txt)
num=42
# Format for displaying a number
txt=f"Number: {num:*>9d}"
print(txt)
# Format for displaying a hexadecimal number
txt=f"Number: {num:#09x}"
print(txt)
txt=f"Number: {num:9x}"
print(txt)
txt=f"Number: {num:*<9x}"
print(txt)
# Format for displaying an octal number
txt=f"Number: {num:*^#09o}"
print(txt)
# Format for displaying a binary number
txt=f"Number: {num:#9b}"
print(txt)