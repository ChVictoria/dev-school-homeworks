x = input("Enter an integer number:")
try:
    x = int(x)
    sum = 0
    if x > 0:
        for i in range(x):
            if not (i % 3 and i % 5):
                sum += i
    print("sum =", sum)
except ValueError:
    print("Input error")
