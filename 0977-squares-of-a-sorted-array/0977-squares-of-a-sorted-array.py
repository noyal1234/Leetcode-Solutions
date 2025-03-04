class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = []
        b = []
        res = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                break
        a = nums[:i][::-1]
        a = [(-1*i) for i in a]
        b = nums[i:]
        i,j = 0,0
        while i < len(a) and j<len(b):
            if a[i] < b[j]:
                res.append(a[i])
                i+=1
            else: 
                res.append(b[j])
                j+=1
        if i < len(a):
            res.extend(a[i:])
        if j < len(b):
            res.extend(b[j:])
        res = [s**2 for s in res]
        return res