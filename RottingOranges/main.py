class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        idea: BFS może być multisource
        """
        queue = deque()
        
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0, 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
                else:
                    continue

        # multi source bfs

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while len(queue) > 0 and fresh > 0:

            sources = len(queue)
            for i in range(sources):
                r, c = queue.popleft()
                # looks at neighbours of specific node
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS and grid[new_r][new_c] == 1:
                        queue.append((new_r, new_c))
                        # rotten it
                        grid[new_r][new_c] = 2
                        fresh -= 1
            # rotting outside nearby sources takes one unit of time
            time += 1
        
        return time if fresh == 0 else -1
        