class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n=len(word)
        cnt=0
        s=set('aeiou')
        for i in range(n):
            for j in range(i+1,n+1):
                if set(word[i:j]) == s:
                    cnt+=1
        return cnt