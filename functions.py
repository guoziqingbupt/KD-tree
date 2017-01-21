import numpy as np


def genSplit(dataMatrix):

    m = dataMatrix.shape[1]
    varList = []

    for d in range(m):
        varList.append(np.var(dataMatrix[:,d]))

    maxVar = max(varList)

    return varList.index(maxVar)


def median(aList):

    n = len(aList)
    if n <= 1:
        return aList[0]

    left, right = 0, n - 1
    index = partition(aList, left, right)

    while index != (n - 1) // 2:
        
        if index < (n - 1) // 2:
            left = index + 1
            index = partition(aList, left, right)
        else:
            right = index - 1
            index = partition(aList, left, right)

    return aList[index]


def partition(aList, left, right):

    if left >= right:
        return left

    pivot = aList[left]

    index = left
    for i in range(left + 1, right + 1):
        if aList[i] < pivot:
            index += 1
            aList[i], aList[index] = aList[index], aList[i]
    aList[left], aList[index] = aList[index], aList[left]
    return index
