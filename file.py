
def modify_content(content):
    
    # Example modification: convert all text to uppercase
    return content.upper()

def main():
    try:
        # Ask the user for the input file name
        input_file = input("Enter the name of the file to read: ")

        # Open the file for reading
        with open(input_file, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Ask the user for the output file name
        output_file = input("Enter the name of the file to write the modified content: ")

        # Write the modified content to a new file
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"Modified content has been written to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_file}' cannot be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
