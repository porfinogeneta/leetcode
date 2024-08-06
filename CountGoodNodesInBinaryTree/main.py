class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def generateTreeUsingList(lst):
    """
    idea: przechodzimy bfsem i na każdym piętrze tworzymy
    nowe nody na podstawie elementów z listy
    :param lst:
    :return:
    """
    # dużo if'ów ale
    nodes = lst[1:]
    tree = TreeNode(lst[0])
    q = [tree]
    while q and nodes:
        node = q.pop(0)
        if node:
            left = nodes.pop(0)
            if left:
                node.left = TreeNode(left)
            if nodes:
                right = nodes.pop(0)
                if right:
                    node.right = TreeNode(right)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return tree




def goodNodes(root):
    """
    :type root: TreeNode
    :rtype: int
    idea: idziemy dfsem i przekazujemy z góry maksymalną wartość,
    jak aktualny korzeń jest mniejszy, to updatujemy maksimum przekazywane niżej,
    na każdym poziomie mamy res (licznik dobrych nodów), który na końcu zwracamy,
    można to też zrobić dając referencję na licznik z zewnętrznej funkcji, np używając listy,
    res[0] = 0
    """

    def countGood(tree, curMax):
        if not tree:
            return 0

        res = 1 if tree.val >= curMax else 0

        curMax = max(curMax, tree.val)
        res += countGood(tree.left, curMax)
        res += countGood(tree.right, curMax)
        return res

    return countGood(root, root.val)

if __name__ == '__main__':
    t = generateTreeUsingList([2,None,4,10,8,None,None,4])
    print(goodNodes(t))
