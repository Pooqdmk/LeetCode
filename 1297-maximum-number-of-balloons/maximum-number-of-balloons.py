class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d=Counter(text)

        word="balloon"

        l=Counter("balloon")
        # if all(letter in d for letter in word) and d['l']>=2 and d['o']>=2:

        #     return min(d[letter] for letter in word)
        return min(d[char]//l[char] for char in word)

    