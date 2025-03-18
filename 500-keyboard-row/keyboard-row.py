class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f="qwertyuiop"
        s="asdfghjkl"
        t="zxcvbnm"
        l=[]
        for i in words:
            if set(i.lower()).issubset(f) or set(i.lower()).issubset(s) or set(i.lower()).issubset(t):
                l.append(i)
        return l