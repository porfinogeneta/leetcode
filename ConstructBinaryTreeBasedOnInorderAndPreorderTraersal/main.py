def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    idea: w preorder pierwszy element to zawsze korzeń, korzystamy z tego
    faktu i ukorzeniamy kolejne drzewa w tym miejscu, z tablicy inorder
    możemy wyciągnąć które elementy są w lewym, a które w prawym poddrzewie,
    korzystając z tego rekurencyjnie rozwiązujemy problem
    """
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    # obliczamy indeks danego korzenia w preorder, żeby zobaczyć które
    # elementy mają być w prawym, które w lewym poddrzewie
    mid = inorder.index(preorder[0])
    # inorder mówi nam ile będziemy mieli elementów w lewym a ile
    # w prawym poddrzewie, czyli mid mówi ile musimy wrzucić elementów
    # z preorder do budowy lewego i prawego poddrzewa
    root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid + 1])
    root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
    return root