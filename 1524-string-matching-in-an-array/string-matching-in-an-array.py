class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s=sorted(words,key=len)
        l=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i] in s[j]:
                    l.append(s[i])
                    break
        return l
            