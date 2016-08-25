"""Collection for all of the sorting algorithms I will code to get a better understanding"""

def insertion_sort(li):
    """Sorts the list li using insertion sort, outputs the sorted list"""
    for i in range(1, len(li)):
        key = li[i]
        j = i - 1
        while j => 0 and li[j] > key:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = key

    return li
