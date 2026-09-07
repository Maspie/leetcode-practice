class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def rot(r,c):
            nonlocal fresh
            if(r < 0 or c < 0 or
                r >= Row or c>=Col or
                grid[r][c] != 1 or (r,c) in visit ):
                return
            q.append((r,c))
            visit.add((r,c))
            fresh -= 1
        Row, Col = len(grid), len(grid[0])

        q = deque()
        time = 0
        fresh = 0
        visit = set()

        for r in range(Row):
            for c in range(Col):

                if grid[r][c] == 2:

                    q.append((r,c))
                    visit.add((r,c))

                elif grid[r][c] == 1:
                    fresh += 1

        
        while q and fresh>0:
            
            for i in range(len(q)):
                R, C = q.popleft()



                rot(R+1, C)
                rot(R-1, C)
                rot(R, C+1)
                rot(R, C-1)
            time += 1
        return time if fresh == 0 else -1










