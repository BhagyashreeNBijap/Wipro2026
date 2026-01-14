# Topic: Functions, Modules (package), File Handling, Exceptions

'''Create a small Python package with:
1. A module containing a function write_numbers_to_file(filename)
2. The function should write numbers 1–100 into a file
3. Handle possible exceptions such as:
File not found
Permission denied
4. Create another module that imports this function and reads the file content safely
x'''

def write_numbers_to_file(filename):
    try:
        with open(filename, "w") as file:
            for i in range(1, 101):
                file.write(str(i) + "\n")
        print("Numbers written successfully.")

    except FileNotFoundError:
        print("Error: File path not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Unexpected error:", e)



def read_file_safely(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File Content:")
            print(content)

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Unexpected error:", e)


#main execution
filename = "numbers.txt"

write_numbers_to_file(filename)
read_file_safely(filename)
