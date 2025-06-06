class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt=0
        for i in str(bin(n)[2:]):
            if i=='1':
                cnt+=1
        return cnt
            