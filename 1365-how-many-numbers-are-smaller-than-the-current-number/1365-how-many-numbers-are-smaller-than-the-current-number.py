class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = {}
        ans = []
        num1 = sorted(nums)
        for i,v in enumerate(num1):
            if v not in a:
                a[v] = i
        for i in nums:
            ans.append(a[i])
        return ans
            