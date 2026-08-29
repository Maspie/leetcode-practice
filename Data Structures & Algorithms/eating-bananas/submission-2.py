class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        res = r
        # 1 - 4 piles
        
        while l <= r:
            time = 0 
            k = (l + r) //2

            for i in piles:

                time += math.ceil(i / k)

            if time <= h:
                
                res = min(res, k)
                r = k - 1

            else:
                l = k + 1
                
        return res

