class Solution:
    def climbStairs(self, n: int) -> int:
        

        # memo = {}

        # def dp(i):
            
        #     if i == n:
        #         return 1

        #     if i > n:
        #         return 0

        #     if i in memo:
        #         return memo[i]

        #     first = dp(i+1)
        #     second = dp(i+2)

        #     memo[i] = first + second

        #     return memo[i]

        # return dp(0)


        one = two = 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one








