from math import sqrt


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    return a**b


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    return sqrt(a)


def combined_formula(a, b):
    return power(divide(multiply(add(a, b), subtract(a, b)), modulo(a, b)), b)


if __name__ == "__main__":
    print("Calculator Demo")
    print("20 + 5 =", add(20, 5))
    print("10 - 5 =", subtract(10, 5))
    print("10 * 5 =", multiply(10, 5))
    print("10 / 5 =", divide(10, 5))
    print("2 ** 3 =", power(2, 3))
    print("10 % 3 =", modulo(10, 3))
    print("sqrt(25) =", square_root(25))
    print("Combined formula (a=5, b=2) =", combined_formula(5, 2))
