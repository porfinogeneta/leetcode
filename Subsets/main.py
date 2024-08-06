def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    idea: Przechodzimy dfsowo po drzewie decyzyjnym,
    drzewo to polega na wyborze dla kolejnych elementów
    czy je brać, czy nie, na końcu, po dojściu do końca
    wyboru elementów, dorzucamy do rozwiązania kopię listy
    """
    res = []
    subset = []

    # i to indeks elementu, który rozważamy czy dodać czy nie
    def dfs(i):
        if i >= len(nums):
            # dodajemy kopię, żeby nie zepsuć tablicy
            # którą modyfikujemy
            res.append(list(subset))
            return

        # na każdej liczbie możemy ją dodać albo nie
        subset.append(nums[i])
        dfs(i + 1)
        # chcemy się po powrocie z dolnej gałęzi dfs cofnąć,
        # wyrzucamy dodany element
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res