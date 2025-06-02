class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1]*len(ratings)
        for i in range(len(ratings)):
            if i!=0 and ratings[i-1] < ratings[i]:
                candy[i] = candy[i-1] + 1

        for i in range(len(ratings)-1,-1,-1):
            if i!= len(ratings)-1 and ratings[i] > ratings[i+1]:
                candy[i]=max(candy[i+1]+1,candy[i])
                print(candy[i])
        return sum(candy)

