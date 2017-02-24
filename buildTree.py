from definitions import *


def buildKdTree(dataMatrix):

    root = KdTreeNode(dataMatrix)

    # there is only one data item in dataMatrix
    if root.data.shape[0] <= 1:
        return root

    helper(root)
    return root


def helper(root):

    if root is None or len(root.data) <= 2:
        return

    # distribute data into left and right
    leftData, rightData = [], []

    # generate left and right child
    for row in list(root.data):
        if row[root.split] <= root.median:
            leftData.append(row)
        else:
            rightData.append(row)

    left = KdTreeNode(np.array(leftData))
    left.parent = root

    right = KdTreeNode(np.array(rightData))
    right.parent = root

    root.data = None
    root.left = left
    root.right = right

    helper(root.left)
    helper(root.right)
