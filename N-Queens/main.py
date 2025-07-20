def solveNQueens(self, n):
    """
    :type n: int
    :rtype: List[List[str]]
    idea: mamy pattern sumy i różnicy na kolicje diagonalne i kolumny, oprócz tego zauważamy
    że mamy jedną królową per rząd, więc na każdym rzędzie mamy n decyzji do podjęcia,
    jak możemy postawić w danym miejscu królową, to ją stawiamy, a potem sprzątamy board i sety
    O(n^2*n!)
    """
    res = []

    cols = set()
    positive_diagonals = set()
    negative_diagonals = set()

    board = [["."] * n for _ in range(n)]

    # backtrack przechodzi po rzędach, po w jednym rzędzie nie może być dwóch królowych
    def backtrack(r):
        if r == n:
            # w wyniku ma być tablica napisów
            copy = ["".join(r) for r in board]
            res.append(copy)
            return

        # w każdym rzędzie możemy postawić po jednym hetmanie, czyli mamy n opcji
        for c in range(n):
            if c in cols or (r - c) in negative_diagonals or (r + c) in positive_diagonals:
                continue  # pomijamy wszystko co zostało w tej iteracji i przechodzimy do kolejnej

            # skoro jest ok, stawiamy królową
            cols.add(c)
            positive_diagonals.add(r + c)
            negative_diagonals.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            # potem czyścimy zbiory i board

            cols.remove(c)
            positive_diagonals.remove(r + c)
            negative_diagonals.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res

