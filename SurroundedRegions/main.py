class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        ROWS, COLS = len(board), len(board[0])
        
        # 1. dfs, find all unsurrounded regions O -> T

        def dfs(r, c):
            # we run dfs from unsurrounded
            # we want to stop if it was visited (board state different than O or it's out of bounds)
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != "O":
                return

            # temporary variable to mark unsurrounded cells
            board[r][c] = "T"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            

        for i in range(ROWS):
            for j in range(COLS):
                if (i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1) and board[i][j] == "O":
                    dfs(i, j)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    # 2. replace all surrounded with x O -> X
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    # 3. replace all temoporary with O, T -> O
                    board[i][j] = "O"
                else:
                    continue
        

        

