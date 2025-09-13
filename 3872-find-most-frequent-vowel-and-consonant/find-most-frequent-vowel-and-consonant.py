class Solution:
    def maxFreqSum(self, s: str) -> int:
        d=Counter(s)
        seen = {'a','e','i','o','u'}
        vowel,c=0,0
        for k,v in d.items():
            if k in seen:
                vowel=max(vowel,v)
            else:
                c=max(c,v)
        return vowel+c
