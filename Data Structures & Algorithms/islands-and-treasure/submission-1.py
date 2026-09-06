class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        Row, Col =  len(grid), len(grid[0])
        visit = set()
        q = deque()
        dist = 0

        for r in range(Row):
            for c in range(Col):

                if grid[r][c] == 0:

                    visit.add((r, c))
                    q.append([r,c])

        def roomt(r, c):

            if (r < 0 or c < 0 or 
                r >= Row or c >= Col or
                 grid[r][c] == -1 or (r, c ) in visit):
                 return
            
            q.append([r,c])
            visit.add((r,c))


        while q:

            for i in range(len(q)):
                R, C = q.popleft()
                grid[R][C] = dist
                roomt(R+1, C)
                roomt(R-1, C)
                roomt(R, C+1)
                roomt(R, C-1)
                
            dist +=1

        

                
