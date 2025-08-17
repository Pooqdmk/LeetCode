class Solution:
    def hIndex(self, c: List[int]) -> int:
        c.sort(reverse = True)
        n=len(c)
        i=n
        while i >= 0:
            cnt=0
            for j in c:
                if j >= i:
                    cnt+=1
                else:
                    break
            if cnt >= i:
                return i
            i-=1
        # return 0

