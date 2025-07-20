def solveNQueens(n):
    cols = set()
    neg_diag = set()
    pos_diag = set()

    board = [["." for _ in range(n)] for _ in range(n)]

    res = []

    def dfs(r, board):
        if r == n:
            res.append(list(board))
            board = [["." for _ in range(n)] for _ in range(n)]
            return

        for c in range(n):
            if c not in cols and (r - c) not in neg_diag and (r + c) not in pos_diag:
                board[r][c] = "Q"
                cols.add(c)
                neg_diag.add(r - c)
                pos_diag.add(r + c)

                dfs(r + 1, board)

                board[r][c] = "."
                cols.remove(c)
                neg_diag.remove(r - c)
                pos_diag.remove(r + c)

        return

    dfs(0, board)

    return res


if __name__ == "__main__":
    solveNQueens(4)