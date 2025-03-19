class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        m=''
        for i in words:
            m+=i[0]
        if m==s:
            return True
        else:
            return False