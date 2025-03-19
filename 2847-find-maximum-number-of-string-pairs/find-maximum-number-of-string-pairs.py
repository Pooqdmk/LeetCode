class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cnt=0
        for i in words:
            if i[::-1]==i:
                continue
            elif i[::-1] in words:
                cnt=cnt+1
        return floor(cnt/2)