class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        premap = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            premap[pre].append(crs)
            indegree[crs] += 1

        
        res = []
        q = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        while q:

            node = q.pop()
            res.append(node)

            for nei in premap[node]:

                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return res if len(res) == numCourses else []


        
        

        