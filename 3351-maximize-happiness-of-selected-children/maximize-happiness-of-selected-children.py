class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        h.sort(reverse = True)
        res = 0
        i,j = 0,0
        while k > 0:
            if h[i] - j > 0:
                res += (h[i] - j)
            else:
                break
            j+=1
            i+=1
            k-=1
        return res
        

