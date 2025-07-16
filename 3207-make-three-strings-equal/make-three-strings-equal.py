class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n1=len(s1)
        n2=len(s2)
        n3=len(s3)
        n=min(n1,n2,n3)
        cnt=0
        for i in range(n):
            if s1[i] == s2[i] == s3[i]:
                cnt+=1
            else:
                break

        return n1-cnt + n2-cnt + n3-cnt if cnt>0 else -1