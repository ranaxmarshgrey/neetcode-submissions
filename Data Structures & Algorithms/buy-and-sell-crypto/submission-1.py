class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxprof=0
        while r<len(prices):
            if prices[r]<prices[l]:
                l=r
                r+=1
            else:
                
                profit=prices[r]-prices[l]
                maxprof=max(maxprof,profit)
                r+=1               

        return maxprof