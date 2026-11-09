"""
Lab 2.3 – Operator Frequency Counter
"""

OPERATORS = ['+', '-', '*', '/', '(', ')']


def count_operators(expression: str) -> dict[str, int]:
    """Return a dictionary containing the count of each operator."""
    counts = {op: 0 for op in OPERATORS}

    for char in expression:
        if char in counts:
            counts[char] += 1

    return counts


if __name__ == "__main__":
    expression = input("Enter an arithmetic expression: ")
    result = count_operators(expression)
    print("Operator counts:", result)
