
def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    O^ m * n * 4^m*n
    """

    # i - wiersz j - kolumna k - litera
    def backtrack(i, j, k):

        if k == len(word):
            return True
        # jak przekraczamy zakres, albo literaz z planszy się nie zgadza
        # to wracamy
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False

        # nie chcemy żeby poprzednia litera była brana pod uwagę
        temp = board[i][j]
        board[i][j] = ""

        if backtrack(i + 1, j, k + 1) or \
                backtrack(i, j + 1, k + 1) or \
                backtrack(i - 1, j, k + 1) or \
                backtrack(i, j - 1, k + 1):
            return True

        board[i][j] = temp
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i, j, 0):
                return True
    return False