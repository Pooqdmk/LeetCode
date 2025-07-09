class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res=0
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n+1,2):
                res+=sum(arr[i:j])
        return res

