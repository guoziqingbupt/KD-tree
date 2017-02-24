from buildTree import *
from readData import *


def text1(fileName):
    dataMatrix = np.array(readData(fileName))
    return buildKdTree(dataMatrix)

if __name__ == "__main__":
    print(text1("testData.csv").right.left.left)
