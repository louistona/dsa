# Sparse Matrix Operations retrieved from the file
from matrix_operations import SparseMatrix, InvalidFormatException

## This program performs operations on sparse matrices
## It reads the matrices from files, performs addition, subtraction, or multiplication
def main():
    try:
        print("Welcome to the program! Choose matrix operation you wish to perform on the matrices:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        choice = int(input("Enter choice (1/2/3): ")) # user input for the operation to be performed

        file1 = input("Enter first matrix file path: ") # user input for the first matrix file path
        file2 = input("Enter second matrix file path: ") # user input for the second matrix file path

        matrix1 = SparseMatrix.from_file(file1) # creating the first matrix object
        matrix2 = SparseMatrix.from_file(file2) # creating the second matrix object

        if choice == 1:
            result = matrix1.addition(matrix2) # addition of the two matrices
        elif choice == 2:
            result = matrix1.subtraction(matrix2) # subtraction of the two matrices
        elif choice == 3:
            result = matrix1.multiplication(matrix2) # multiplication of the two matrices
        else:
            print("Invalid choice.")
            return

        print("Result (non-zero elements):")
        for (r, c), v in sorted(result.data.items()):
            print(f"({r}, {c}, {v})") # printing the result of the operation

    except InvalidFormatException as e:
        print("ERROR:", str(e))
    except Exception as e:
        print("Unexpected error:", str(e)) # general error handling

# This is the entry point of the program
if __name__ == "__main__":
    main()
