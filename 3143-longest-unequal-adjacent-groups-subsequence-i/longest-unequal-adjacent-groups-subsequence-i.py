class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res=[]
        res.append(groups[0])
        r=[]
        r.append(words[0])
        for i in range(1,len(words)):
            if groups[i] != res[-1]:
                res.append(groups[i])
                r.append(words[i])
        return r

