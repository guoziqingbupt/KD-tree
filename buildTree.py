from definitions import *
from functions import *
import copy


def buildKdTree(root):

    if root.data.shape[0] <= 1:
        return root
    root.split = genSplit(root.data)
    root.left, root.right = genChildren(root)
    buildKdTree(root.left)
    buildKdTree(root.right)


def genChildren(root):

    valOnTheDimension = list(root.data[:, root.split])
    med = median(valOnTheDimension)

    leftData, rightData = [], []

    for row in list(root.data):
        if row[root.split] <= med:
            leftData.append(row)
        else:
            rightData.append(row)

    leftMaxPoint = copy.deepcopy(root.rect.maxPoint)
    leftMaxPoint[root.split] = med
    leftRect = Hyperrctangle(root.rect.minPoint, leftMaxPoint)
    left = KdTreeNode(np.array(leftData), leftRect)

    rightMinPoint = copy.deepcopy(root.rect.minPoint)
    rightMinPoint[root.split] = med
    rightRect = Hyperrctangle(rightMinPoint, root.rect.maxPoint)
    right = KdTreeNode(np.array(rightData), rightRect)

    return left, right