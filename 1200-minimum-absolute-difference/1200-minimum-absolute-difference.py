class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        mindiff=float('inf')
        res = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                mindiff = min(mindiff,abs(arr[i]-arr[j]))
        arr.sort()
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if abs(arr[i]-arr[j]) == mindiff:
                    res.append([arr[i],arr[j]])
        return res