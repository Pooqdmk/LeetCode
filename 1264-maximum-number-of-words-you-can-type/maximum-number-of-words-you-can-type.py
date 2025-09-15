class Solution:
    def canBeTypedWords(self, text: str, bl: str) -> int:
        l=text.split()
        cnt=0
        s=set(bl)
        for i in l:
            valid=True
            for j in i:
                if j in s:
                    valid=False
                    break
            if valid:
                cnt+=1

        return cnt
        