class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        if not grid:
            return 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        Row, Col = len(grid), len(grid[0])
        visit = set()
        MaxArea = 0
        
        def bfs(r, c):
            area = 1
            q = deque()

            q.append((r,c))
            visit.add((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    R, C = row + dr, col + dc

                    if (R < 0 or C < 0 or R >= Row or C >= Col or 
                        grid[R][C] != 1 or (R,C) in visit):
                        continue

                    q.append((R, C))
                    visit.add((R, C))
                    area += 1
            return area




        for r in range(Row):
            for c in range(Col):

                if grid[r][c] == 1 and (r, c) not in visit:

                    area = bfs(r, c)
                    MaxArea = max(area, MaxArea)

        return MaxArea

