class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        cnt=0
        n=len(hours)
        for i in range(n):
            for j in range(i+1,n):
                if (hours[i]+hours[j])%24==0:
                    cnt+=1
        return cnt