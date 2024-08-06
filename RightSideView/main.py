def rightSideView(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        idea: zrobić bfs i wrzucać na każdym piętrze ostani element (najbardziej na prawo)
        """
        res = []
        if root == None: return []
        q = [root]
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == qLen - 1:
                    res.append(node.val)
        return res