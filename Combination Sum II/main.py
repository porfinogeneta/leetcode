def combinationSum2(self, candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    idea: na każdej liczbie mamy dwie opcje, bierzemy albo nie bierzemy,
    jeśli bierzemy to dodajemy do kombinacji, zwiększamy sumę, jeśli nie bierzemy,
    to musimy pominąć wszystkie duplikaty tej liczby w candidates, bo nie chcemy, żeby
    wystąpiła kombinacja z daną liczbą raz jeszcze
    """
    res = []

    candidates.sort()  # sortujemy, żeby powtórki były obok siebie

    # i -> wskaźnik na kandydata
    def dfs(i, current_sum, current_comb):
        # znaleźliśmy dobrą sumę
        if current_sum == target:
            res.append(list(current_comb))
            return
        # przekroczyliśmy zakres, za duża suma
        if i >= len(candidates) or current_sum > target:
            return

        # bierzemy obecną
        current_comb.append(candidates[i])
        dfs(i + 1, current_sum + candidates[i], current_comb)
        # nie bierzemy obecnej liczby, ale chcemy się przesunąć do kolejnej innej
        current_comb.pop()
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        dfs(i + 1, current_sum, current_comb)

    dfs(0, 0, [])
    return res