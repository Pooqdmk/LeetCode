class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        s={'a','e','i','o','u'}
        cnt=0
        for i in words[left:right+1]:
            if set(i[0]).issubset(s) and set(i[len(i)-1]).issubset(s):
                cnt=cnt+1
        return cnt