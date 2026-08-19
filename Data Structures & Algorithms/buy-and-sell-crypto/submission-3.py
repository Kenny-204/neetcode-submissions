class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0,1
        maxProfit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]

            if profit > maxProfit:
                maxProfit = profit 
            elif profit < 0 :
                left = right
                right+=1
            else:
                right+=1
        return maxProfit 