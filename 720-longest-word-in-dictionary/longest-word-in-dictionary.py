class Solution:
    def longestWord(self, words: List[str]) -> str:
        res=""
        w=set(words)
        for i in words:
            if all(i[:j] in w for j in range(1,len(i)+1)):
                if len(i)>len(res) or (len(i) == len(res) and i<res):
                    res=i
        return res