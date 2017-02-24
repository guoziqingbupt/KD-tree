import math


def dis(item, query):
    """
    calculate the distance between query and a data item
    :param item: ndarray value
    :param query: ndarray value
    :return: distance
    """
    return math.sqrt((item - query) @ (item - query))


def search(root, query, result, minDis):

    cur = root

    # the root is None
    if not cur:
        return result

    # find leaf
    elif not cur.visited:
        while cur.left and cur.right:
            if query[cur.split] >= cur.median:
                cur = cur.right
            else:
                cur = cur.left

        # update the min dis if it is necessary
        for item in list(cur.data):
            tempDis = dis(item, query)
            if abs(tempDis - minDis) < 1e-9:
                result.append(list(item))
            elif tempDis < minDis:
                minDis = tempDis
                result = [list(item)]


        # update the visited
        cur.visited = True

        # process the next node
        cur = findNextNode(cur)
        if intersect(cur, query, minDis):
            return search(cur, query, result, minDis)
        else:
            cur.visited = True
            nextNode = findNextNode(cur)
            return search(nextNode, query, result, minDis)
    else:
        return result


def findNextNode(cur):
    if cur.parent is None:
        return
    par = cur.parent
    # find the next node that to be search
    while par and par.left.visited and par.right.visited:
        par.visited = True
        cur = par
        par = par.parent
    return getBrother(cur)


def intersect(node, query, radius):
    par = node.parent
    return abs(query[par.split] - par.median) <= radius


def getBrother(node):
    """
    get the node's brother if it has.
    :param node:
    :return:
    """
    if node.parent is None:
        return None
    if node is node.parent.left:
        return node.parent.right
    else:
        return node.parent.left
