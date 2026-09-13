class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}

        def dp(i):
            
            if i >= len(cost):
                return 0



            if i in memo:
                return memo[i]

            # take
            first = cost[i] + dp(i+1)

            #skip to 2
            second = cost[i] + dp(i+2)

            memo[i] = min(first, second)

            return memo[i]

        return min(dp(0), dp(1))