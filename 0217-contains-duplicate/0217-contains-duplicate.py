class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq=defaultdict(int)
        out = False
        for num in nums:
            freq[num]+=1
        print(freq.keys())
        for i in freq.keys():
            if freq[i]<2 and out != True:
                out = False
            else:
                out = True
        return out