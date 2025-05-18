class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo={}
        return self.Comb(amount,coins,0,memo)
    
    def Comb(self, amount:int,coins: List[int],index:int,memo:dict):
        
        if (amount,index) in memo:
            return memo[(amount,index)]
        if amount == 0:
            return 1
        if amount < 0 or index==len(coins):
            return 0
        take = self.Comb(amount-coins[index],coins,index,memo)
        skip = self.Comb(amount,coins,index+1,memo) 
        memo[(amount,index)] = take+skip
    
        return memo[(amount,index)]