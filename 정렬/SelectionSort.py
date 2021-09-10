def selectionSort(x):
    length = len(x)
    for i in range(length - 1):
        indexMin = i
        for j in range(i + 1, length):
            if x[indexMin] > x[j]:
                indexMin = j
        x[i], x[indexMin] = x[indexMin], x[i]
    return x
