def largest_radial_sum(arr, d):
    n = len(arr)
    if n % d != 0 or d not in range(1, 32):
        print("Invalid input!")
        return

    space = int(n/d)
    greatest_honor = sum([arr[i] for i in range(0,len(arr),space)])
    for j in range(1, space):
        honor = sum([arr[i] for i in range(j,len(arr),space)])
        if honor > greatest_honor:
            greatest_honor = honor

    return greatest_honor


print(largest_radial_sum([1,5,6,3,4,2],3))