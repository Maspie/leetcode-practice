class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        premap = defaultdict(list)
        visit = set()

        for crs, pre in prerequisites:
            premap[crs].append(pre)

        def dfs(crs):

            if crs in visit:
                return False

            if premap[crs] == []:
                return True

            visit.add(crs)

            for i in premap[crs]:
                if not dfs(i):
                    return False

            visit.remove(crs)
            premap[crs] = []

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

            

