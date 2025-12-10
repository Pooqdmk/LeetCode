class Solution:
    def countPermutations(self, c: List[int]) -> int:
        def fact(n):
            x = 1
            for i in range(2,n+1):
                x*=i
            return x
        n = len(c)
        for i in range(1,n):
            if c[i] <= c[0]:
                return 0

        return fact(n-1)%(10**9 + 7)