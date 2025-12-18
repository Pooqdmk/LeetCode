class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        pre = [0]*(n+1)
        l = [0]*(n+1)

        for i in range(1,n+1):
            pre[i] = pre[i-1] + (prices[i-1]*strategy[i-1])
            l[i] = l[i-1] + prices[i-1]
        # print(pre, l)
        gain = 0
        original = pre[-1]
        for r in range(k,n+1):
            left = r-k
            mid = k//2 + left
            new_win = l[r] - l[mid]
            old_win = pre[r] - pre[left]

            gain = max(gain, new_win - old_win)
        return original + gain
