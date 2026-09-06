class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0

        Row, Col = len(grid), len(grid[0])
        islands = 0
        visit = set()
        directions = [[1,0], [-1,0], [0,1], [0, -1]]
        def bfs(r, c):

            q = deque()
            visit.add((r, c))
            q.append((r,c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:

                    newR, newC = dr + row, dc + col

                    if ( newR < 0 or newC < 0 or 
                            newR >= Row or newC >= Col or
                            grid[newR][newC] != "1" or (newR, newC) in visit):
                            continue
                    
                    q.append((newR, newC))

                    visit.add((newR, newC))

                 





        for r in range(Row):
            for c in range(Col):

                if grid[r][c] == "1" and (r,c) not in visit:

                    bfs(r,c)

                    islands += 1

        return islands