class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        for num in set(nums):
            if nums.count(num) == 1:
                uniq = num
        return uniq