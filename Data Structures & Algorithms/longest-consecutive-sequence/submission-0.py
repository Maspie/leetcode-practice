class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # for this we need to check if a number before exists to know if its a start number. Then we keep track of how long a seq goes with a while look and increamenting the number and trying to find the next number in set

        longest = 0
        seq = set(nums)

        for i in range(len(nums)):
            length = 0
            if (nums[i] - 1) not in seq:
                j = nums[i]
                while j in seq:
                    length += 1
                    j += 1
            
            longest = max(length, longest)

        return longest






