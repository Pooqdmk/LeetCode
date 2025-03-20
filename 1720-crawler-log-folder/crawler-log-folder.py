class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt=0
        for i in logs:
            if i=='../':
                cnt=cnt-1
            elif i=='./':
                continue
            else:
                cnt=cnt+1
            if cnt<0:
                cnt=0
        # if cnt>0:
        return cnt
        # else:
        #     return 0
    
