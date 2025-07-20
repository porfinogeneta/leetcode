def subsetsWithDup(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    idea: robimy drzewo decyzyjne, jak dla problemu Subsets, z tą różnicą,
    że jak nie dodajemy duplikatu, to pomijamy wszystkie duplikaty, liczby
    wejściowe oczywiście sortujemy żeby duplikaty były obok siebie.
    Duplikaty pojawiają się tylko gdy próbujemy dodać zduplikowaną liczbę
    w jakimś subsetcie, w którym wcześniej z niej zrezygnowaliśmy
    O(n * 2^n + nlogn)
    """
    nums.sort()
    res = []

    # i -> indeks, z listy nums, subs -> obecny subset
    def backtrack(i, subs):
        if i >= len(nums):
            res.append(list(subs))
            return

        # dodajemy obecną liczbę
        subs.append(nums[i])
        backtrack(i + 1, subs)
        subs.pop()

        # pomijamy obecną liczbę i wszystkie jej duplikaty
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        backtrack(i + 1, subs)

    backtrack(0, [])
    return res
