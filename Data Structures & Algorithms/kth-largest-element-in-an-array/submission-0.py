class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        maxheap = [-num for num in nums]

        heapq.heapify(maxheap)

        while k > 0:

            element = -heapq.heappop(maxheap)

            k -= 1


        return element