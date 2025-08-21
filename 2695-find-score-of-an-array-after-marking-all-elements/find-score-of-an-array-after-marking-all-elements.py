class Solution:
    def findScore(self, nums: List[int]) -> int:
        n=len(nums)
        mark=[False]*n
        cnt=0

        heap = [(nums[i],i) for i in range(n)]
        heapq.heapify(heap)

        while heap:
            mn,ind = heapq.heappop(heap)
            
            if mark[ind]:
                continue
            cnt+=mn
            if ind-1 >=0:
                mark[ind-1]=True
            if ind+1 < n:
                mark[ind+1]=True
            mark[ind]=True
        return cnt