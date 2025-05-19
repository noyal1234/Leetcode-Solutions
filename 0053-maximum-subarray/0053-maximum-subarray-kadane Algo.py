class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        i=0
        for num in nums:
            dp[i] = max(num,dp[i-1]+num)
            i+=1
        return max(dp)