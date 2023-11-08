from math import floor
import sys
sys.setrecursionlimit(1000)

def descending_order(x):
    digits = []

    while x > 0:
        digits.append(x % 10)
        x = floor(x / 10)

    try:
        digits = quick_sort(digits, 0.5)
    except RecursionError:
        try:
            digits = quick_sort(digits, 0)
        except RecursionError:
            print("Stack overflow")
            return

    y = 0
    n = 0
    for d in digits:
        y += d*10**n
        n += 1

    return y

def quick_sort(arr, pivot_coeff):

    if len(arr) <= 1:
        return arr

    pivot = arr[floor(len(arr)*pivot_coeff)]
    arr.remove(pivot)
    smaller = [elem for elem in arr if elem <= pivot]
    bigger = [elem for elem in arr if elem > pivot]

    return quick_sort(smaller, pivot_coeff)+[pivot]+quick_sort(bigger, pivot_coeff)



print(descending_order(int(input("Input x:"))))
