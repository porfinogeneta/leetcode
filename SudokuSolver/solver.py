


board = [["", "", 8, "", "", "", 1, 7, ""],
         ["", "", "", "", 2, "", "", "", ""],
         [9, 3, "", "", "", 1, "", "", 4],
         [7, "", 5, 4, "", 2, "", "", ""],
         [1, "", "", "", "", "", "", "", 9],
         ["", "", "", 7, "", 3, 4, "", 6],
         [3, "", "", 6, "", "", "", 4, 2],
         ["", "", "", "", 5, "", "", "", ""],
         ["", 8, 7, "", "", "", 6, "", ""]]



def solve(board):


    valid_pos = [(i, j) for i in range(9) for j in range(9) if board[i][j] != ""]

    def is_valid(board):


        # check squares
        squares = [[[] for _ in range(3)] for _ in range(3)]

        
        for i in range(len(board)):
            for j in range(len(board)):
                sq_row = i // 3
                sq_col = j // 3
                if board[i][j] != "":

                    if board[i][j] in squares[sq_row][sq_col]:
                        return False
                    squares[sq_row][sq_col].append(board[i][j])

                
       
        for i in range(9):
            # row                         
            row = set()
            for j in range(9):
                if board[i][j] in row:
                    return False
                elif board[i][j] != "":
                    row.add(board[i][j])

        # col 
        # for j in range(9):
        #     col = set()
        #     for i in range(9):
        #         if board[i][j] in col:
        #             return False
        #         elif board[i][j] != "":
        #             col.add(board[i][j])
        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] in col:
                    return False
                elif board[i][j] != "":
                    col.add(board[i][j])

        return True
    
    # is_valid(board)

    def is_board_full(board):
        for row in board:
            if "" in row:
                return False
        return True
    

    def backtrack(board, r, c):


        if is_board_full(board):
            return board

        if not is_valid(board) or r == 9:
            return None
        

        if (r, c) in valid_pos:
            if c == 8:
                next_r, next_c = r + 1, 0
            else:
                next_r, next_c = r, c + 1
            return backtrack(board, next_r, next_c)

       
     
        for n in range(1, 10):
            # try to place the number
            board[r][c] = n
            if c == 8:
                next_r, next_c = r + 1, 0
            else:
                next_r, next_c = r, c + 1
            b = backtrack(board, next_r, next_c)

            if b is not None:
                return b
            
            board[r][c] = ""

        return None

            
    return backtrack(board, 0, 0)

    
if __name__ == "__main__":

    print("Solving Sudoku...")
    for row in board:
        print(row)

    solved_board = solve(board)
    if solved_board:
        print("\nSolved Sudoku:")
        for row in solved_board:
            print(row)
