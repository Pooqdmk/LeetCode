class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s=sorted(letters)

        for i in s:
            if i>target:
                return i
        return letters[0]