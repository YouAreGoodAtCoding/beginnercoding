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
# O(m+n) where m is length of arr1 and n is length of arr2
# there are other ways with same complexity too, like using + operator,
# create a new list and appending items one at a time to the new list.
###


def combineLists(l1: list, l2: list):
    # res = l1 just assigns reference.
    res = l1.copy()
    res.extend(l2)
    return res


if __name__ == "__main__":
    # test combine
    # [1, 3, 5], [2, 4, 6] → [1, 3, 5, 2, 4, 6]
    l1 = [1, 3, 5]
    l2 = [2, 4, 6]
    res = combineLists(l1, l2)

    print(f"{l1} and {l2} combined gives {res}")

    arr1 = array.array('i', l1)
    arr2 = array.array('i', l2)
    res = combineIntArrays(arr1, arr2)

    print(f"{arr1} and {arr2} combined gives {res}")

    # test merge
    arr1 = array.array('i', [])
    arr2 = array.array('i', [])
    res = mergeSortedIntArrays(arr1, arr2)
    print(f"{arr1} and {arr2} merged gives {res}")

    arr1 = array.array('i', [1, 3, 5, 7, 8, 9, 23])
    arr2 = array.array('i', l2)
    res = mergeSortedIntArrays(arr1, arr2)
    print(f"{arr1} and {arr2} merged gives {res}")
