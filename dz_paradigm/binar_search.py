def binary_search(aray, search):
    start_element = aray[0]
    end_element = len(aray) - 1
    while start_element <= end_element:
        middle_element = start_element + (end_element - start_element) // 2
        if aray[middle_element] == search:
            return middle_element
        elif aray[middle_element] < search:
            start_element = middle_element + 1
        else:
            end_element = middle_element - 1
    return -1

arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

print(binary_search(arr, 13))


