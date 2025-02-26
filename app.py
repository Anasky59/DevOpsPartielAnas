def add(a, b):
    """Ajoute deux nombres."""
    return a + b


def multiply(x, y):
    """Multiplie deux nombres."""
    return x * y


def divide(x, y):
    """Divise x par y si y n'est pas zéro."""
    if y != 0:
        return x / y


def greet(name):
    """Retourne un message de salutation."""
    if name == "":
        return "Hello, World!"
    else:
        return "Hello, " + name
