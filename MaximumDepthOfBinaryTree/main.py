def maxDepth( root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # rekurencyjny dfs
    # if root == None:
    #     return 0
    # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    # bfs
    # if root == None:
    #     return 0
    # queue = [root]
    # depth = 0
    # while queue:
    #     for i in range(len(queue)):
    #         fst = queue.pop(0)
    #         if fst.left:
    #             queue.append(fst.left)
    #         if fst.right:
    #             queue.append(fst.right)
    #     depth += 1
    # return depth
    # iteracyny dfs
    stack = [[root, 1]]
    mx = 0
    while stack:
        node, depth = stack.pop()

        if node:
            mx = max(depth, mx)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])

    return mx