# Specify the path to the text file you want to read
file_path = "sample_data1.txt"

try:
    # Open the file for reading (by default, it's in read mode 'r')
    with open(file_path, 'r') as file:
        # Read the file line by line into a list of lines
        lines = file.readlines()

        # Display the content or perform any desired operations
        print("File Content:")
        for line in lines:
            print(line, end="")  # Print each line without adding extra newlines

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
