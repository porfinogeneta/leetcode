class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        idea: Sprawdzamy dokąd można dojść z pierwszego wiersza i pierwszej kolumny (wszystkie dostępne dla Atlantyku pola),
        potem dokąd z ostatniego wiersza i ostatniej kolumny i na koniec bierzemy przekrój
        """
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()


        def dfs(r, c, height, visited):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or heights[r][c] < height:
                return
            visited.add((r,c))
            dfs(r-1, c, heights[r][c], visited)
            dfs(r+1, c, heights[r][c], visited)
            dfs(r, c+1, heights[r][c], visited)
            dfs(r, c-1, heights[r][c], visited)

        for c in range(COLS):
            dfs(0, c, heights[0][c], atl)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], pac)

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], atl)
            dfs(r, COLS-1, heights[r][COLS - 1], pac)


        result = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in atl:
                    result.append([i,j])

        return result