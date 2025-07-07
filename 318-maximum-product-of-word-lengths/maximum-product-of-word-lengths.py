class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mx=0
        d={i:set(i) for i in words}
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if d[words[i]].isdisjoint(d[words[j]]):
                    mx=max(mx,len(words[i])*len(words[j]))

        return mx

