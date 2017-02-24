from readData import *
from search import *
from buildTree import *


def main(fileName):

    # make the 2-dimensional list into ndarray matrix
    dataMatrix = np.array(readData(fileName))

    # construct kd tree
    root = buildKdTree(dataMatrix)

    # give the query
    query = np.array([8, 3])

    # minDis: negative infinity
    minDis = float("inf")

    # initialize the result as None
    result = []

    return search(root, query, result, minDis)


if __name__ == "__main__":
    print(main("testData.csv"))
