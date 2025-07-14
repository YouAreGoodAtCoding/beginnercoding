import array


# warm up
# Arrays are more memory-efficient than lists for large amounts of homogeneous data, as it does not store pointers to objects.
def combineIntArrays(arr1: array, arr2: array):
    # res = arr1 just assigns reference.
    res = array.array('i', arr1)
    for i in range(len(arr2)):
        # Cannot assign directly to index that is more than initial size or perform resizing explicitly.
        # Amortized O(1) using append(), supports resizing by over allocation.
        res.append(arr2[i])

    # this also works and has same complexity.
    # res.extend(arr2)
    return res


###
# O(m+n) where m is length of arr1 and n is length of arr2
# there are other ways with same complexity too, like using + operator,
# create a new list and appending items one at a time to the new list.
###
def combineLists(l1: list, l2: list):
    # res = l1 just assigns reference.
    res = l1.copy()
    res.extend(l2)
    return res


###
# warmup: fill from end, assuming we have enough places at the end of arr1 to hold elements of arr2.
# arr1 = [1, 2, 3, 0, 0, 0]
# arr2 = [4, 5, 6]
# arr1 = [1, 2, 3, 4, 5, 6]
###
def combineArraysInplace(arr1: array, arr2: array):
    i2 = len(arr2)-1
    i1 = len(arr1)-1
    while (i2 >= 0 and i1 >= 0):
        arr1[i1] = arr2[i2]
        i1 -= 1
        i2 -= 1


# main challenge
# merge two sorted arrays
# [1, 3, 5], [2, 4, 6] → [1, 2, 3, 4, 5, 6]
# time O(n + m), where n and m are the lengths of the arrays.
# space O(n + m)
###
def mergeSortedIntArrays(arr1: array, arr2: array):
    # preallocate sufficient space for efficiency
    size = len(arr1) + len(arr2)
    res = array.array('i', [0] * size)
    i1 = i2 = i = 0

    # start looking at elements starting from first and which ever is lower, copy that over to res, and increment that pointer
    while (i1 < len(arr1) and i2 < len(arr2)):
        if (arr1[i1] <= arr2[i2]):
            res[i] = arr1[i1]
            i1 += 1
        else:
            res[i] = arr2[i2]
            i2 += 1
        i += 1

    # if there are elements remaining in arr1, simply copy that over
    while (i1 < len(arr1)):
        res[i] = arr1[i1]
        i += 1
        i1 += 1

    # if there are elements remaining in arr2, simply copy that over
    while (i2 < len(arr2)):
        res[i] = arr2[i2]
        i += 1
        i2 += 1

    return res


###
# main challenge
# nums1 = [1, 3, 5, 0, 0, 0]
# m = 3  # number of real elements in nums1
# nums2 = [2, 4, 6]
# n = 3  # number of elements in nums2
# nums1 = [1, 2, 3, 4, 5, 6]
###
def mergeSortedIntArraysInPlace(arr1: array, m: int, arr2: array, n: int):
    i = m-1
    j = n-1
    k = m+n-1

    # if arr1 finishes first, arr2 needs to be copied over, so do until j reaches start.
    # if arr2 finishes first, rest of arr1 is already in arr1 and need not be copied over.
    while (j >= 0):
        if (i >= 0 and arr1[i] > arr2[j]):
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1


if __name__ == "__main__":
    # test combine  (in a new list/array)
    # [1, 3, 5], [2, 4, 6] → [1, 3, 5, 2, 4, 6]
    l1 = [1, 3, 5]
    l2 = [2, 4, 6]
    res = combineLists(l1, l2)

    print(f"{l1} and {l2} combined gives {res}")

    arr1 = array.array('i', l1)
    arr2 = array.array('i', l2)
    res = combineIntArrays(arr1, arr2)

    print(f"{arr1} and {arr2} combined gives {res}")

    # test merge (in a new array)
    arr1 = array.array('i', [])
    arr2 = array.array('i', [])
    res = mergeSortedIntArrays(arr1, arr2)
    print(f"{arr1} and {arr2} merged gives {res}")

    arr1 = array.array('i', [1, 3, 5, 7, 8, 9, 23])
    arr2 = array.array('i', [2, 4, 6])
    res = mergeSortedIntArrays(arr1, arr2)
    print(f"{arr1} and {arr2} merged gives {res}")

    # test combine  (inplace)
    # [1, 3, 5, 0, 0, 0], [2, 4, 6] , arr1 modified to [1, 3, 5, 2, 4, 6]
    arr1 = array.array('i', [1, 3, 5])
    arr2 = array.array('i', [2, 4, 6])
    arr1.extend([0] * len(arr2))
    print(f"Combining {arr1} and {arr2} in place")
    combineArraysInplace(arr1, arr2)
    print(f"arr1 is now: {arr1}")

    # test merge (inplace)
    # empty
    arr1 = array.array('i', [])
    arr2 = array.array('i', [])
    m = len(arr1)
    n = len(arr2)
    arr1.extend([0] * n)
    print(f"Merging {arr1} and {arr2} in place")
    mergeSortedIntArraysInPlace(arr1, m, arr2, n)
    print(f"arr1 is now: {arr1}")

    # interspersed
    arr1 = array.array('i', [1, 3, 5, 8, 10])
    arr2 = array.array('i', [2, 4, 6])
    m = len(arr1)
    n = len(arr2)
    arr1.extend([0] * n)
    print(f"Merging {arr1} and {arr2} in place")
    mergeSortedIntArraysInPlace(arr1, m, arr2, n)
    print(f"arr1 is now: {arr1}")

    # arr1 has bigger elements, so arr1 will run out of index first
    arr1 = array.array('i', [4, 9])
    arr2 = array.array('i', [1, 2, 3])
    m = len(arr1)
    n = len(arr2)
    arr1.extend([0] * n)
    print(f"Merging {arr1} and {arr2} in place")
    mergeSortedIntArraysInPlace(arr1, m, arr2, n)
    print(f"arr1 is now: {arr1}")

    # arr2 has bigger elements, so arr2 will run out of index first
    arr1 = array.array('i', [1, 2, 3, 4])
    arr2 = array.array('i', [4, 9, 10, 11, 12])
    m = len(arr1)
    n = len(arr2)
    arr1.extend([0] * n)
    print(f"Merging {arr1} and {arr2} in place")
    mergeSortedIntArraysInPlace(arr1, m, arr2, n)
    print(f"arr1 is now: {arr1}")

    # arr1 and arr2 is exactly same
    arr1 = array.array('i', [21, 21])
    arr2 = array.array('i', [21, 21])
    m = len(arr1)
    n = len(arr2)
    arr1.extend([0] * n)
    print(f"Merging {arr1} and {arr2} in place")
    mergeSortedIntArraysInPlace(arr1, m, arr2, n)
    print(f"arr1 is now: {arr1}")
