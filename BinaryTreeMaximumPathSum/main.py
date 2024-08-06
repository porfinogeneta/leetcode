def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    idea: zejść dfs i poczynając od lisći obliczyć na każdym piętrze maksimum
    i porównać z globalnym maksimum
    """
    globalMax = [float("-inf")]

    def dfs(root):
        if not root: return 0

        rightVal = dfs(root.right) if root.right else 0
        leftVal = dfs(root.left) if root.left else 0

        # na każdym piętrze chcemy zwrócić maksymalną wartość
        # root.val + rightVal + leftVal oznacza że możemy się podzielić na dwa kierunki,
        # obliczamy to tylko do zupdatowania globalnego maximum,
        # nie zawsze tak jednak będzie, więc rekurencyjnie chcemy zwrócić maximum tylko z
        # root.val, root.val + rightVal, root.val + leftVal (root.val, bo nikt nam nie każe brać danego elementu)
        maximumValue = max([root.val, root.val + rightVal, root.val + leftVal, root.val + rightVal + leftVal])
        globalMax[0] = max(maximumValue, globalMax[0])
        return max([root.val, root.val + rightVal, root.val + leftVal])

    dfs(root)
    return globalMax[0]