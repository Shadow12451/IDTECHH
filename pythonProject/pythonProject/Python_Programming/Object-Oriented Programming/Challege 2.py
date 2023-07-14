entries = [32, 14, 89, 62, 10, 20, 88, 40, 22,  91, 88, 65]
def bubble_sort(values):
    for i in range(len(values) - 1):
        for j in range(0, len(values) - 1):
            if values[j] > values[j + 1]:
                temp = values[j]
                values[j] = values[j + 1]
                values[j + 1] = temp
    return values
print(bubble_sort(entries))