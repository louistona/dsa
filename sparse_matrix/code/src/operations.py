# Error class in case of invalid input format
class InvalidFormatException(Exception):
    pass

# Creating the sparse matrix class
class SparseMatrix:

    # initializing objects in the sparse matrix
    def __init__(self, rows=0, cols=0):
        self.rows = rows
        self.cols = cols
        self.data = {}  # key: (row, col), value: number

    # reading the file and creating the sparse matrix
    @staticmethod
    def from_file(filepath):
        matrix = SparseMatrix()
        with open(filepath, 'r') as f: # opening the file
            lines = f.readlines()
        try:
            matrix.rows = int(lines[0].strip().split('=')[1]) # getting the number of rows
            matrix.cols = int(lines[1].strip().split('=')[1]) # getting the number of columns
        except:
            raise InvalidFormatException("Input file has wrong format") # error in case of wrong format

        # check if the number of rows and columns are within the limit
        for line in lines[2:]:
            line = line.strip().replace(' ', '') # removing spaces
            if not line:
                continue
            if not (line.startswith('(') and line.endswith(')')):
                raise InvalidFormatException("Input file has wrong format") # error in case of wrong format
            parts = line[1:-1].split(',')
            if len(parts) != 3:
                raise InvalidFormatException("Input file has wrong format") # error in case of wrong format
            try:
                row, col, val = int(parts[0]), int(parts[1]), int(parts[2])
            except:
                raise InvalidFormatException("Input file has wrong format") # error in case of wrong format
            matrix.set_element(row, col, val)
        return matrix

    # getting the number of rows and columns
    def get_element(self, row, col):
        return self.data.get((row, col), 0)

    # setting the number of rows and columns
    def set_element(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

# the operations that will be performed on the sparse matrix
# addition, multiplication and subtraction

    # addition of two sparse matrices
    def addition(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix size above the limit for addition")
        result = SparseMatrix(self.rows, self.cols)
        for (r, c), v in self.data.items():
            result.set_element(r, c, v)
        for (r, c), v in other.data.items():
            result.set_element(r, c, result.get_element(r, c) + v)
        return result

    # multiplication of two sparse matrices
    def multiplication(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix size above the limit for multiplication!")
        result = SparseMatrix(self.rows, other.cols)
        for (r, c), val1 in self.data.items():
            for i in range(other.cols):
                val2 = other.get_element(c, i)
                if val2 != 0:
                    current = result.get_element(r, i)
                    result.set_element(r, i, current + val1 * val2)
        return result

    # subtraction of two sparse matrices
    def subtraction(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix size is above the limit for subtraction!")
        result = SparseMatrix(self.rows, self.cols)
        for (r, c), v in self.data.items():
            result.set_element(r, c, v)
        for (r, c), v in other.data.items():
            result.set_element(r, c, result.get_element(r, c) - v)
        return result