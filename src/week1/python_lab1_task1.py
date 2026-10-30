"""
Task 1: Calculate the area of a circle.

Examples:
>>> round(circle_area(2), 2)
12.57
>>> circle_area(0)
0.0
"""

import math


def circle_area(radius: float) -> float:
    """Return the area of a circle given its radius (unrounded)."""
    return math.pi * radius**2


if __name__ == "__main__":
    radius = float(input("Enter the circle radius: "))
    area = circle_area(radius)
    print(f"Circle area: {area:.2f}")
