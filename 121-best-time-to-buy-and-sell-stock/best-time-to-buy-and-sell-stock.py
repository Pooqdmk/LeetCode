class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # m=min(prices)
        # for i in range(len(prices)):
        #     if m==prices[i]:
        #         index=i
        #         break

        # h=max(prices[index:])
        # return h-m

        m=float('inf')
        pro=0
        for i in prices:
            m=min(i,m)
            pro=max(pro,i-m)
        return pro




