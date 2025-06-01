class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        for i in range(0,(n//(limit+1))+1):
            sign= (-1)**i
            term = comb(3,i)*comb(n-i*(limit+1)+2,2)
            count += sign*term
        return count