def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    idea: zrobić bfs i wrzucić wyniki do res
    """
    res = []
    queue = [root]
    while queue:
        h = []
        qLen = len(queue)
        for i in range(qLen):
            node = queue.pop(0)
            if node:
                h.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        if h:
            res.append(h)
    return res