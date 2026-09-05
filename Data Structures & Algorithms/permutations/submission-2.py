class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []

        def  backtrack():

            if len(nums) == len(path):
                res.append(path.copy())

                return

            for i in range(len(nums)):

                if nums[i] in path:
                    continue
                path.append(nums[i])

                backtrack()

                path.pop()

        backtrack()

        return res