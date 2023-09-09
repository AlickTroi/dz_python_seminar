#  Напишите программу, которая сортирует список чисел методом сортировки слиянием.

def merge_list(array_a, array_b):
    c = []
    first = len(array_a)
    second = len(array_b)

    i = 0
    j = 0
    while i < first and j < second:
        if array_a[i] <= array_b[j]:
            c.append(array_a[i])
            i += 1
        else:
            c.append(array_b[j])
            j += 1

    c += array_a[i:] + array_b[j:]
    return c

def split_and_merge_list(a):
    N1 = len(a) // 2
    left = a[:N1]    
    right = a[N1:]

    if len(left) > 1: 
        left = split_and_merge_list(left)
    if len(right) > 1: 
        right = split_and_merge_list(right)

    return merge_list(left, right)   


a = [9, 5, 1, 3, 13, -5, -7, 5, 9, 3, -10, 9, 5, -3, 4, 7, 8, -8]
a = split_and_merge_list(a)

print(a)