class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        w=sorted(word,reverse=True)
        cnt=0
        seen=set()
        for i in w:
            if i.isupper() and i not in seen:
                seen.add(i)
                if i.lower() in word:
                    cnt+=1
        return cnt