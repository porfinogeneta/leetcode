def isSubtree(self, root, subRoot):
    """
    idea: na każdym wierzchołku sprawdzamy czy poddrzewo jest równe danemu drzewu,
    ukorzenionemu w aktualnym wierzchołku -> złożoność O(n*m)
    n - # wierzchołków w root, m - # wierzchołków w subRoot
    """
    if subRoot == None: return True
    if root == None: return False
    if self.isSameTree(root, subRoot):
        return True
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


def isSameTree(self, t1, t2):
    if t1 == None and t2 == None:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)