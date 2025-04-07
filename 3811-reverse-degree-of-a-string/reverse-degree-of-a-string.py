class Solution:
    def reverseDegree(self, s: str) -> int:
        d={}
        index=26
        for i in range(ord('a'),ord('z')+1):
            d[chr(i)]=index
            index-=1
        sum=0
        for i in range(len(s)):
            sum+=d[s[i]]*(i+1)
        return sum
        