from buildTree import *
from readData import *


def main(fileName):

    dataMatrix = np.array(readData(fileName))

    minPoint, maxPoint = [0, 0], [10, 10]
    rootRect = Hyperrctangle(minPoint, maxPoint)

    root = KdTreeNode(dataMatrix, rootRect)

    buildKdTree(root)
    return root


if __name__ == "__main__":
    root = main("testData.csv")
    print(root)
