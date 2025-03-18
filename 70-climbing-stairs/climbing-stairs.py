class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,2
        li=[1,2]
        for i in range(n):
            li.append(a+b)
            a,b=b,a+b
        return li[n-1]