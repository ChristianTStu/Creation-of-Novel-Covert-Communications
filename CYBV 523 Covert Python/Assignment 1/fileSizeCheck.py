import os


def compare_file_sizes(file1, file2):
    size1 = os.path.getsize(file1)
    size2 = os.path.getsize(file2)

    size_difference = abs(size1 - size2)

    if size1 < size2:
        return f"{file1} is {size_difference} bytes smaller than {file2}."
    elif size1 > size2:
        return f"{file1} is {size_difference} bytes larger than {file2}."
    else:
        return f"{file1} and {file2} have the same size."


# Example usage
file1 = "C:/Users/Christian/Documents/GitHub/UoA-Python-Projects/CYBV 523 Covert Python/Test Images/test_original.png"
file2 = "C:/Users/Christian/Documents/GitHub/UoA-Python-Projects/CYBV 523 Covert Python/Test Images/test_modified.png"

result = compare_file_sizes(file1, file2)
print(result)
