class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a=Counter(words1)
        k=[key for key,value in a.items() if value==1]

        b=Counter(words2)
        l=[key for key,value in b.items() if value==1]

        return len(set(k) & set(l))