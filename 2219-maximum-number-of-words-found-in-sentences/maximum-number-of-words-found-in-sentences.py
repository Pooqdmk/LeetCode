class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max=0
        for i in sentences:
            if max<len(i.split()):
                max=len(i.split())
        return max