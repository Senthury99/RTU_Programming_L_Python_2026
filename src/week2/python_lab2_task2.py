
"""
Lab 2.2 – Comprehensions and Transformations
"""

NUMBERS = [3, 8, -2, 7, 0, -5, 10]


def squares(numbers: list[int]) -> list[int]:
    """Return the square of each number."""
    return [number ** 2 for number in numbers]


def positives(numbers: list[int]) -> list[int]:
    """Return only positive numbers."""
    return [number for number in numbers if number > 0]


def even_squares(numbers: list[int]) -> set[int]:
    """Return squares of even numbers."""
    return {number ** 2 for number in numbers if number % 2 == 0}


def cubes(numbers: list[int]) -> dict[int, int]:
    """Return a dictionary mapping numbers to their cubes."""
    return {number: number ** 3 for number in numbers}


if __name__ == "__main__":
    print("Squares:", squares(NUMBERS))
    print("Positives:", positives(NUMBERS))
    print("Even squares:", even_squares(NUMBERS))
    print("Cubes:", cubes(NUMBERS))
