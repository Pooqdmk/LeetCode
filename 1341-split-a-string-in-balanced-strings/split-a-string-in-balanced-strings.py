class Solution:
    def balancedStringSplit(self, s: str) -> int:
        i=0
        cnt=0
        while i<len(s):
            d= Counter(s[:i+1])
            if 'R' and 'L' in d:
                if d['R']==d['L']:
                    cnt+=1
            i+=1

        return cnt