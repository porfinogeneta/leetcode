# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def flipEquiv(self, root1, root2):
    """
    :type root1: Optional[TreeNode]
    :type root2: Optional[TreeNode]
    :rtype: bool
    idea: schodzimy dfs'em i sprawdzamy czy jak przestawimy dzieci, albo ich nie przestawimy czy otrzymamy
    takie same drzewa
    O(|V|) -> przechodzimy po wszystkich wierzchołkach
    """

    if root1 == None and root2 == None:
        return True

    if ((root1 == None or root2 == None) or root1.val != root2.val):
        return False

    # patrzymy czy jest ok bez albo z przepięciem
    return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))
            or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
            )