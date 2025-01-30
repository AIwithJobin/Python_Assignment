#Exercise 1
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("File not found.")

# Example usage:
read_file("example.txt")




#Exercise 2
def copy_file(source, destination):
    try:
        with open(source, 'r') as src_file:
            contents = src_file.read()
        with open(destination, 'w') as dest_file:
            dest_file.write(contents)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Source file not found.")

# Example usage:
copy_file("source.txt", "destination.txt")



#Exercise 3
def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()
            words = contents.split()
            print(f"Total number of words: {len(words)}")
    except FileNotFoundError:
        print("File not found.")

# Example usage:
count_words_in_file("example.txt")



#Exercise 4
def convert_to_int():
    user_input = input("Enter a number: ")
    try:
        num = int(user_input)
        print(f"The integer is {num}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Example usage:
convert_to_int()



#Exercise 5
def check_negative_integers():
    try:
        user_input = input("Enter a list of integers (comma-separated): ")
        int_list = [int(x) for x in user_input.split(',')]
        for num in int_list:
            if num < 0:
                raise ValueError("Negative integer detected.")
        print("All integers are non-negative.")
    except ValueError as e:
        print(f"Error: {e}")

# Example usage:
check_negative_integers()



#Exercise 6
def compute_average():
    try:
        user_input = input("Enter a list of integers (comma-separated): ")
        int_list = [int(x) for x in user_input.split(',')]
        average = sum(int_list) / len(int_list)
        print(f"The average is: {average}")
    except ValueError:
        print("Invalid input. Please enter valid integers.")
    except ZeroDivisionError:
        print("The list cannot be empty.")
    finally:
        print("Program execution finished.")

# Example usage:
compute_average()




#Exercise 7
def write_to_file():
    file_name = input("Enter the filename: ")
    text = input("Enter the text to write to the file: ")
    try:
        with open(file_name, 'w') as file:
            file.write(text)
        print("Text written to file successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Welcome! No exceptions occurred.")

# Example usage:
write_to_file()

