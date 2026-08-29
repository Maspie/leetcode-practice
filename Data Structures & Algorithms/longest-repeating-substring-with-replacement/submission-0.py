class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0

        count = {}

        freq = 0
        l = 0
        for r in range(len(s)):

            count[s[r]] = 1 + count.get(s[r], 0)
            freq = max( freq, count[s[r]])

            if (r - l + 1) - freq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
