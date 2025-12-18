class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        pre = [0]*n
        pre[0] = prices[0]*strategy[0]
        l = [0]*n
        l[0] = prices[0]
        for i in range(1,n):
            pre[i] = pre[i-1] + (prices[i]*strategy[i])
            l[i] = l[i-1]+prices[i]
        res = -10**60
        for i in range(k-1,n):
            if i-k >= 0:
                left = pre[i-k]
            else:
                left = 0
            right = pre[-1] - pre[i]
            if i-k // 2 >= 0:
                curr = l[i] - l[i-(k//2)]
            else:
                curr = 0
            res = max(res, left+right+curr)
        return max(res, pre[-1])


        