
class Hyperrctangle(object):

    def __init__(self, minPoint, maxPoint):
        """
        generating hyperrctangle based on maxPoint and minPoint
        :param maxPoint: a m-dimensional list
        :param minPoint: a m-dimensional list
        """
        self.minPoint = minPoint
        self.maxPoint = maxPoint
        self.content = []

    def fillRect(self, points):

        for point in points:
            self.content.append(point)


class KdTreeNode(object):

    def __init__(self, dataMatrix, rect):

        self.data = dataMatrix
        self.rect = rect
        self.left, self.right = None
        self.split = None
