def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    idea: robimy drzewo decyzyjne każdy wierzchołek daje max 4 wybory na litery, potem
    przechodzimy dfs po tym drzewie, dodając litery do wyniku
    złożoność: O(n*4^n)
    -> mamy 4^n outputów, a długość każdej ścieżki to n, czyli żeby znaleźć wynik
    musieliśmy przejść 4^n ścieżek, każda o długości n
    """

    keypad_dict = {
        "1": [],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
        "0": []
    }

    res = []
    comb = []

    def dfs(d_idx):

        if d_idx == len(digits):
            s = "".join(comb)
            if s:
                res.append(s)
            return

        for l in keypad_dict[digits[d_idx]]:
            comb.append(l)
            dfs(d_idx + 1)
            comb.pop()

    dfs(0)

    return res