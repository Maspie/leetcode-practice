class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # premap = defaultdict(list)
        # visit = set()

        # for crs, pre in prerequisites:
        #     premap[crs].append(pre)

        # def dfs(crs):

        #     if crs in visit:
        #         return False

        #     if premap[crs] == []:
        #         return True

        #     visit.add(crs)

        #     for i in premap[crs]:
        #         if not dfs(i):
        #             return False

        #     visit.remove(crs)
        #     premap[crs] = []

        #     return True

        # for i in range(numCourses):
        #     if not dfs(i):
        #         return False

        # return True

        premap = defaultdict(list)
        visit = set()
        indegree = [0] * numCourses
 
        for crs, pre in prerequisites:
            premap[crs].append(pre)
            indegree[pre] += 1

        count = 0

        q = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)


        while q:

            node = q.popleft()

            count += 1
            for nei in premap[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)


        return count == numCourses
            

