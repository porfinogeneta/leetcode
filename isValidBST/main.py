def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    idea: Przechodzimy dfs i przekazujemy na każdym piętrze zakresy dostępnych liczb
    """

    def dfs(root, minRange, maxRange):
        if root == None:
            return True
        if root.val < minRange or root.val > maxRange:
            return False
        if minRange < root.val < maxRange:
            return dfs(root.left, minRange, root.val) and dfs(root.right, root.val, maxRange)

    return dfs(root, float("-inf"), float("inf"))