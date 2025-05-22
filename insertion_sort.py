def insertion_sort(array):
    for j in range(1, len(array)):
        # j = 1, i = 0
        i = j - 1
        key = array[i + 1]
        while i >= 0 and array[i] > key:
            tmp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = tmp
            i = i - 1

    return array


arr = [7, 4, 9, 5, 1]
print(insertion_sort(arr))
