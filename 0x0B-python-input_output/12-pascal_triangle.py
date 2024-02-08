#!/usr/bin/python3

"""A module to generate Pascal's triangle up to the nth row."""

def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.

    This function generates Pascal's triangle up to the nth row. Each row of the triangle
    is represented as a list of integers. The first row (n=0) contains only one element,
    which is 1. Subsequent rows are constructed using the binomial coefficient formula.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]  # First element is always 1
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):  # Iterate over previous row
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle

# Test the function
if __name__ == "__main__":
    print(pascal_triangle(5))
