class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d=Counter(words[0])
        for i in words[1:]:
            d=d& Counter(i)
        return list(d.elements())
        

        