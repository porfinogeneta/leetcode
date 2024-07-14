def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    idea: schodzimy po bst, jak dwie ścieżki się rozdzielają, albo korzeń == p lub q
    to znaczy, że musi to być wspólny przodek, bo takie rozdzielenie/równość powoduje,
    że nie znajdziemy później przodka
    """
    cur = root
    while cur:
        if cur.val > p.val and cur.val > q.val:
            cur = cur.left
        elif cur.val < p.val and cur.val < q.val:
            cur = cur.right
        else:
            # elementy się rozdzielają albo są równe, to znaczy że to jest nasz przodek
            return cur