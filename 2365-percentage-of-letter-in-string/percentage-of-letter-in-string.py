class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        d=Counter(s)

        return floor((d[letter]*100)/len(s))