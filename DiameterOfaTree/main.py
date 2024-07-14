def diameterOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    mx = [0]

    # dfs policzy nam wysokość, potem aktualizujemy diamater na jej podstawie
    def dfs(root):
        if root == None:
            return -1

        left = dfs(root.left)
        right = dfs(root.right)

        mx[0] = max(mx[0], 2 + left + right)

        return 1 + max(left, right)

    dfs(root)
    return mx[0]