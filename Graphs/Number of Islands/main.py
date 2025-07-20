def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    idea: przechodzimy po całej planszy, jak znajdziemy "1" to puszczamy z tej "1" DFS
    jak znajdziemy "1" która nie była dotychczas w odwiedzonych za pomocą dfs, zwiększamy counter wysp
    """
    islands = 0
    visited = set()

    def dfs(row, col):
        stack = [(row, col)]
        while stack:
            x, y = stack.pop()
            visited.add((x, y))
            # sprawdzamy sąsiadów
            # góra
            if x > 0 and (x - 1, y) not in visited and grid[x - 1][y] == '1':
                stack.append((x - 1, y))
            # dół
            if x < len(grid) - 1 and (x + 1, y) not in visited and grid[x+1][y] == '1':
                stack.append((x + 1, y))
            # prawo
            if y < len(grid[0]) - 1 and (x, y + 1) not in visited and grid[x][y+1] == '1':
                stack.append((x, y + 1))
            # lewo
            if y > 0 and (x, y - 1) not in visited and grid[x][y - 1] == '1':
                stack.append((x, y - 1))

    for n in range(len(grid)):
        for m in range(len(grid[0])):
            if (n, m) not in visited and grid[n][m] == '1':
                islands += 1
                dfs(n, m)

    return islands


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]


    print(numIslands(grid))