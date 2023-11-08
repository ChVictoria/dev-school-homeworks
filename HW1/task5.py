def high_and_low(string):
    numbers = [int(i) for i in string.split()]
    return str(max(numbers))+" "+str(min(numbers))


print(high_and_low(input("Input numbers, separated by space:")))
