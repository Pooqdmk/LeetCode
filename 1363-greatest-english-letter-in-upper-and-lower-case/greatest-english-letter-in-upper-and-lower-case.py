class Solution:
    def greatestLetter(self, s: str) -> str:
        seen=set(s)
        l=sorted(seen,reverse=True)
        
        for i in l:
            if i.isupper():
                if i.lower() in l:
                    return i
        return ''
        