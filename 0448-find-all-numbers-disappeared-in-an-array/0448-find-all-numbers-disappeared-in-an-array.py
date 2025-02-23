class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = set(nums)
        miss = []
        n = len(nums)
        for i in range(1,n+1):
            if i not in a :
                miss.append(i)
        return miss