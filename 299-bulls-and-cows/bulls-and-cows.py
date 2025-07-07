class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnt=0
        cows=0
        s=list(secret)
        l=list(guess)
        n=len(secret)
        for i in range(n):
            if secret[i] == guess[i]:
                cnt+=1
                s.remove(secret[i])
                l.remove(guess[i])

        for i in l:
            if i in s:
                cows+=1
                s.remove(i)

        return str(cnt)+'A'+str(cows)+'B'