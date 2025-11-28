class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        e,o = 0,0
        s = 0
        res = 0
        for i,n in enumerate(arr):
            s+=n
            if s%2 == 0:
                e+=1
                res+=o
            else:
                o+=1
                res += 1+e
        return res%(10**9 + 7)


            