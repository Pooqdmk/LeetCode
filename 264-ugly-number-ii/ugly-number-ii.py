class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = [1]
        visit = set()

        for i in range(n):
            num = heapq.heappop(h)

            if i == n-1:
                return num
            
            for j in [2,3,5]:
                if j*num not in visit:
                    visit.add(j*num)
                    heapq.heappush(h,j*num)
            