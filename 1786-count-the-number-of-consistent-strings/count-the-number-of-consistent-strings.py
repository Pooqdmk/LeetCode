class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt=0
        for i in words:
            if set(i).issubset(set(allowed)):
                cnt=cnt+1
        return cnt