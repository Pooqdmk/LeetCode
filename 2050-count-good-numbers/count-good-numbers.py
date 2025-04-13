class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # e=[0,2,4,6,8]
        # o=[2,3,5,7]
        even=(n+1)//2
        odd=n//2
        mod=10**9+7
        cnt=(pow(5,even,mod)*pow(4,odd,mod))%mod
        return cnt

        