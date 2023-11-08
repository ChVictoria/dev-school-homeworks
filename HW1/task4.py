from math import sqrt, ceil


def is_prime(x):

    if x <= 1:
        return False

    if x == 2 or x == 3:
        return True

    if x % 2 == 0 or x % 3 == 0:
        return False

    for i in range(5, ceil(sqrt(x))+1, 6):
        if x % i == 0 or x % (i+2) == 0:
            return False
    return True


x = input("Enter an integer number:")
try:
    x = int(x)
    print(is_prime(x))
except ValueError:
    print("Input error")
