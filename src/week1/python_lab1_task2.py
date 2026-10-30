"""
Task 2: Clean and format a user's name.
"""


def greet_user(name: str) -> str:
    """Return a greeting message after cleaning and capitalizing the name."""
    clean_name = name.strip().capitalize()

    if clean_name == "":
        clean_name = "Stranger"

    return f"Hello, {clean_name}! Welcome to Python!"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet_user(name))
