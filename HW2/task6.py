def land_perimeter(arr):
    perimeter = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'X':
                perimeter += 4
                if i != len(arr)-1:
                    if arr[i+1][j]  == 'X':
                        perimeter -= 2
                if j != len(arr[i])-1:
                    if arr[i][j + 1] == 'X':
                        perimeter -= 2

    return "Total land perimeter: " + str(perimeter)

print(land_perimeter(['XOOXO',
                     'XOOXO',
                     'OOOXO',
                     'XXOXO',
                     'OXOOO']))