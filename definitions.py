import numpy as np


class KdTreeNode(object):

    def __init__(self, dataMatrix):

        self.data = dataMatrix

        self.left, self.right = None, None
        self.parent = None

        self.split = self.getSplit()
        self.median = self.getMedian()

        self.visited = False

    def getSplit(self):

        # the number of column of dataMatrix, it is also the number of dimension of matrix
        col_num = self.data.shape[1]

        # varList records all variances of column vector
        varList = []
        for d in range(col_num):
            varList.append(np.var(self.data[:, d]))

        # get the maximum variance
        maxVar = max(varList)

        # return the dimension sequence we want.
        return varList.index(maxVar)

    def getMedian(self):

        # get a list that stored all values of the split dimension
        valOnTheDimension = list(self.data[:, self.split])

        # get the median of the list above
        n = len(valOnTheDimension)
        if n <= 1:
            return valOnTheDimension[0]

        left, right = 0, n - 1
        index = self.partition(valOnTheDimension, left, right)

        while index != (n - 1) // 2:

            if index < (n - 1) // 2:
                left = index + 1
                index = self.partition(valOnTheDimension, left, right)
            else:
                right = index - 1
                index = self.partition(valOnTheDimension, left, right)

        # return the median
        return valOnTheDimension[index]

    def partition(self, aList, left, right):

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
