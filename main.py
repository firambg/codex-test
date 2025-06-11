"""Main module with greeting function."""

from typing import Optional

def greet(name: Optional[str] = None) -> str:
    """Return a greeting message for the given name.

    If no name is provided, return a generic greeting.
    """
    if name:
        return f"Привет, {name}!"
    return "Привет!"

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        print(greet(sys.argv[1]))
    else:
        print(greet())
