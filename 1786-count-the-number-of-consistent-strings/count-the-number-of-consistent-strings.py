class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s=set(allowed)
        # cnt=0
        # for i in words:
        #     if set(i).issubset(s):
        #         cnt=cnt+1
        return sum(set(i).issubset(s) for i in words )