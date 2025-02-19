class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i,j in enumerate(nums):
            if i != j:
                return i
        if i == len(nums)-1:
            return i+1
        