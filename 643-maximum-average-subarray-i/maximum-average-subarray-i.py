class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pre = [0]
        t = 0
        for i in nums:
            t+=i
            pre.append(t)
        mx = -10**60
        print(pre)
        for i in range(len(nums)-k+1):
            print(pre[i+k] - pre[i])
            mx = max(mx, (pre[i+k] - pre[i])/k)
        return mx


        