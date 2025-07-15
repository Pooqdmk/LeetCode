class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cnt=0
        l=text.split()
        for i in l:
            present=False
            for j in i:
                if j in brokenLetters:
                    present=True
            if not present:
                cnt+=1
        return cnt
