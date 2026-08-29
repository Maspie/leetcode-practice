class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        Count = {}
        arr = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            Count[nums[i]] = 1 + Count.get(nums[i], 0)
        res = []
        for i, n in Count.items():

            arr[n].append(i)

        for i in range(len(arr) -1, 0, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res



        