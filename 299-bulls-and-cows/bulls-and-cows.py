class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # cnt=0
        # cows=0
        # s=list(secret)
        # l=list(guess)
        # n=len(secret)
        # for i in range(n):
        #     if secret[i] == guess[i]:
        #         cnt+=1
        #         s.remove(secret[i])
        #         l.remove(guess[i])

        # for i in l:
        #     if i in s:
        #         cows+=1
        #         s.remove(i)
        d=Counter(secret)
        cnt,cows=0,0
        n=len(secret)
        for i in range(n):
            if secret[i]==guess[i]:
                cnt+=1
                d[secret[i]]-=1 

        for i in range(n):
            if secret[i]!=guess[i] and d[guess[i]] > 0:
                cows+=1
                d[guess[i]]-=1

        return str(cnt)+'A'+str(cows)+'B'