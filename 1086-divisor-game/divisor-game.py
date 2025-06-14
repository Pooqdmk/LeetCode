class Solution:
    def divisorGame(self, n: int) -> bool:
        # def divisors(n):
        #     l=[]
        #     for i in range(math.sqrt(n)+1):
        #         if n%i==0:
        #             l.append(i)
        #             l.append(n//i)

        #     l.sort()
        #     return l

        # d=divisors(n)
        # for i in d:
        #     if i<n:
        #         n=n-i
        #         m=divisors(n)

                
        return n%2==0