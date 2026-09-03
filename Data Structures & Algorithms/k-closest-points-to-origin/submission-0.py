class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        minheap = [(x*x + y*y, x, y) for x, y in points] 
        res = []
        heapq.heapify(minheap)

        while k:

            a, b, c = heapq.heappop(minheap)

            res.append([b,c])

            k -= 1

        return res

