
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


def serialize(self, root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    idea: przejść bfs po drzewie uzysując taką samą,
    strukturę jak ta leetocdowa, tylko że w stringu
    """
    serialized = ""
    q = [root]
    while q:
        ll = len(q)
        for i in range(ll):
            node = q.pop(0)

            if node:
                serialized += str(node.val) + " "
                q.append(node.left)
                q.append(node.right)
            else:
                serialized += "null" + " "
    return serialized


def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    idea: brzydka deserializacja do tablicy,
    potem idziemy porządkiem bfs i dodajemy do kolejki kolejne
    utworzon drzewa, i popujemy ze zbioru wartości do dodania, tj. des
    """
    des = []
    for e in data.split(" "):
        if e == "null":
            des.append(None)
        else:
            try:
                des.append(int(e))
            except ValueError:
                pass
    if des[0] == None: return []
    t = TreeNode(des[0])
    des = des[1:]
    q = [t]
    while q and des:
        cur = q.pop(0)
        valL = des.pop(0)
        if valL != None:
            cur.left = TreeNode(valL)
            q.append(cur.left)
        valR = des.pop(0)
        if valR != None:
            cur.right = TreeNode(valR)
            q.append(cur.right)
    return t


# DFS
"""
    idea: przechodzimy dfs preorder i wrzucamy do stringa
"""
def serialize(self, root):
    ser = []

    def dfs(root):
        if root == None:
            ser.append("N")
            return
        ser.append(str(root.val))
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return ",".join(ser)

"""
    idea: przechodzimy preorder po tej tablicy zserailizowanej
"""
def deserialize(self, data):
    des = data.split(",")
    self.i = 0 # indeks aktualnego elementu z des
    def dfs():
        if des[self.i] == "N":
            # przesuwamy się w naszej tablicy
            self.i += 1
            return None
        node = TreeNode(int(des[self.i]))
        self.i += 1
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()

if __name__ == '__main__':
    t = generateTreeUsingList([1,2,3,None,None,4,5])
    ser = serialize(t)
    dt = deserialize(ser)