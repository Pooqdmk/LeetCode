class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        n = len(strs)
        fixed = [False]*(n-1)
        for j in range(len(strs[0])):
            found = False
            for i in range(n-1):
                if not fixed[i] and strs[i][j] > strs[i+1][j]:
                    found = True
                    break
            if found:
                cnt+=1
                continue
            for i in range(n-1):
                if not fixed[i] and strs[i][j] < strs[i+1][j]:
                    fixed[i] = True
        return cnt
