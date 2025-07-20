def combinationSum(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    idea: przechodzimy dfs po drzewie decyzyjnym, które powstało,
    poprzez decyzje, czy wziąć daną liczbę czy nie, tworzyliśmy ścieżki
    używające albo nie używające konkrentnej ilości liczb
    """
    res = []

    # i -> którą liczbę chcemy dodać/ nie chcemy dodać (pointer)
    # cur_comb -> obecna kombinacja
    # cur_sum -> do czego sumuje się nasza obecna kombinacja
    def dfs(i, cur_comb, cur_sum):
        # base case
        if cur_sum == target:
            res.append(list(cur_comb))  # dajemy kopię, bo rekurencja używa tej listy
            return
        # nie ma już możliwości dobierania rzeczy albo za duża suma
        if i >= len(candidates) or cur_sum > target:
            return

        cur_comb.append(candidates[i])
        # pierwsza ścieżka dodajemy duplikat naszej liczby
        dfs(i, cur_comb, cur_sum + candidates[i])
        # druga ścieżka, decydujemy się nie brać tej liczby
        cur_comb.pop()
        dfs(i + 1, cur_comb, cur_sum)

    dfs(0, [], 0)
    return res


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(combinationSum(candidates, target))