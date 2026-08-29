class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0
        res = 0
        duplicates = set()
        while r < len(s):

            while s[r] in duplicates:
                
                duplicates.remove(s[l])
                l += 1

            duplicates.add(s[r])

            res = max(r-l+1, res)

            r += 1

        return res