#!/usr/bin/env python3.12
#https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python

import pprint
from typing import Iterable, Generator


def get_side_lengths(base: int) -> Generator:
    """Calculate lenghts of the spiral sides"""

    for s in [base, base, base]:
        yield s
    for s in [base - b for b in range(2, base, 2) ]:
        yield s
        yield s


def rotate_vector_counter_clockwise(vector: tuple[int, int]) -> tuple[int, int]:
    """Calculate rotation vector to make spiral direction"""

    # Rotation matrix for 90 degrees clockwise
    rotation_matrix = [[0, 1], [-1, 0]]

    # Vector to be rotated (x, y)
    x, y = vector

    # Perform matrix multiplication
    x_prime = rotation_matrix[0][0] * x + rotation_matrix[0][1] * y
    y_prime = rotation_matrix[1][0] * x + rotation_matrix[1][1] * y

    return (x_prime, y_prime)


def get_side_coords_set(
    origin_point: tuple[int, int], direction: tuple[int, int], side_steps: int
) -> Iterable[tuple[int, int]]:
    """Calculate matrix coordinated for a spiral side"""

    yield origin_point
    for _ in range(side_steps - 2):
        origin_point = origin_point[0] + direction[0], origin_point[1] + direction[1]
        yield origin_point


def get_initial_matrix(size: int) -> list[list[int]]:
    """Create matrix by the given sixe and fill with 0"""
    return [ [0] * size for _ in range(size) ]


def spiralize(size: int) -> list[list[int]]:
    """Returns matrix by the given size with a spiral of '1'"""

    # Fill initial matrix with 0
    spiral = get_initial_matrix(size)
    pprint.pprint(spiral)

    print([s for s in get_side_lengths(size)])

    # Start coordinates and direction as a unit verctor
    origin_point = 0, 0
    direction = 0, 1

    # Fill the matrix with 1 side by side the spiral
    for side in get_side_lengths(size):
        print([x for x in get_side_coords_set(origin_point, direction, side)])

        # Calculate spiral coordinates based on the given matrix size with step=2
        # and fill the current side of the spiral with 1
        for point in get_side_coords_set(origin_point, direction, side):
            spiral[point[0]][point[1]] = 1

        # Get current point in the matrix - the last element of the spiral side
        origin_point = origin_point[0] + direction[0] * (side - 1), \
                       origin_point[1] + direction[1] * (side - 1)

        # Calculate direction as a unit vector: (0, 1) | (1, 0) | (0, -1) | (-1, 0)
        # of the next spiral side:
        direction = rotate_vector_counter_clockwise(direction)

    return spiral


def main():
    N = 10
    spiral = spiralize(N)
    pprint.pprint(spiral)


if __name__ == "__main__":
    main()
