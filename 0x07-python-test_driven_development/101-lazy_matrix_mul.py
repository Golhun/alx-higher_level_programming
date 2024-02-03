#!/usr/bin/python3
"""
Matrix multiplication
"""


def lazy_matrix_mul(m_a, m_b):
    """
    A Function which multiplies two matrices.

    Arguments:
    - m_a: First matrix (list of lists of integers/floats)
    - m_b: Second matrix (list of lists of integers/floats)

    Returns:
    - The product of the matrices (list of lists)

    Raises:
    - TypeError: If m_a or m_b is not a list of lists, if an element in the
                matrices is not an integer or a float, or if the matrices are
                not rectangles (all rows must be of the same size).
    - ValueError: If m_a and m_b can't be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if any(not isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    
    if any(not isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")
    
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b) for row in m_b):
        raise TypeError("each row of m_a must be of the same size" +
                        " or each row of m_b must be of the same size")
    
    answer = [[0 for i in range(len(m_b[0]))] for i in range (len(m_a))]

    for i in range(len(m_a)):
        for m in range(len(m_b[0])):
            for o in range(len(m_b)):
                answer[i][m] += m_a[i][o] * m_b[o][m]

    return answer