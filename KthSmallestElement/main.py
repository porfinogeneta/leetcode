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

def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        idea: inorder traversal + wrzucenie elementów do tablicy,
        rozwiązanie iteracyjne + rekurencyjne
        """
        n = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

        # res = []
        # def inorder(root):
        #     if root == None:
        #         return None

        #     inorder(root.left)
        #     res.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # return res[k-1]


if __name__ == '__main__':
    t = generateTreeUsingList([3,1,4,None,2])
    print(kthSmallest(t, 1))