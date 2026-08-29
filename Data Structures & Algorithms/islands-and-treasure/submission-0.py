class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROW = len(grid)
        COL = len(grid[0])
        q = deque()
        INF = 2147483647
        for r in range(ROW):
            for c in range(COL):

                if grid[r][c] == 0:
                    q.append((r,c))

        
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                R, C = dr + r, dc + c

                if (0 <= R < ROW and 0 <= C < COL and grid[R][C] == INF):

                    grid[R][C] = grid[r][c] + 1
                    q.append((R,C)) 

        
        
        