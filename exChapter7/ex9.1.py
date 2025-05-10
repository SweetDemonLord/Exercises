def main():
    # Requesting a file name from the user
    file_name=input("Enter a name of a text file: ")
    try:
        # Open the entered file for reading
        with open(file_name,"r") as original_file:
            lines=original_file.readlines()

        # Show content of the original file
        print("Content of the file:")
        for line in lines:
            print(line.strip())
        # Create a copy of the file with numbered lines
        numbered_file_name="numbered_" + file_name
        with open(numbered_file_name,"w") as numbered_file:
            for idx, line in enumerate(lines,1):
                numbered_file.write(f"{idx}:{line}")
        print(f"The copy of the file with numbered lines: {numbered_file_name}:")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__=="__main__":
    main()