class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        res = [words[0]]
        for i in words[1:]:
            if sorted(i) != sorted(res[-1]):
                res.append(i)
        return res
