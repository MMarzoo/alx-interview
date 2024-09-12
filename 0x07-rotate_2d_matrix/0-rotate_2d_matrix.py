#!/usr/bin/python3
"""
2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """
    2D matrix, rotate it 90 degrees clockwise.
    """
    # Step 1: Transpose the matrix (swap rows with columns)
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Step 2: Reverse each row to complete the 90-degree clockwise rotation
    for row in matrix:
        row.reverse()
