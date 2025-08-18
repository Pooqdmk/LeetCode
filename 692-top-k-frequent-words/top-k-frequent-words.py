class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=Counter(words)
        l=dict(sorted(d.items(),key=lambda x:(-x[1],x[0])))

        return list(l.keys())[:k]
