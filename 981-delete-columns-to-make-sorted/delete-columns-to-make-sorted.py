class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        cnt = 0
        for i in range(m):
            r = []
            for j in range(n):
                r.append(strs[j][i])
            # print(r)
            if r != sorted(r):
                cnt+=1
        return cnt


            