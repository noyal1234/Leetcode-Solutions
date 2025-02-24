class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=0
        while i < len(nums) and j < len(nums):
            if i!=j and nums[i] + nums[j] == target:
                return [i,j]
            elif j == len(nums)-1:
                i+=1
                j = i+1
            else:
                j+=1