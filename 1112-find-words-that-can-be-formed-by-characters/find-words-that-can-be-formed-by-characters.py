class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d=Counter(chars)
        t=0
        for i in words:
            cnt=Counter(i)
            if all(cnt[char]<=d[char] for char in i):
                t+=len(i)
        return t