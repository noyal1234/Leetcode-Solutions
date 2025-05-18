class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        return self.path(n,memo)
    def path(self,n: int,memo: dict):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if n in memo:
            return memo[n]
        oneStep = self.path(n-1,memo)
        twoStep = self.path(n-2,memo)
        memo[n] = oneStep+twoStep
        return memo[n]