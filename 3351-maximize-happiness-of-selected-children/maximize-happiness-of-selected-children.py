class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        res = 0
        i,j = 0,0
        while k > 0:
            if happiness[i] - j > 0:
                res += (happiness[i] - j)
            else:
                break
            j+=1
            i+=1
            k-=1
        return res


