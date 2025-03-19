class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        l=[]
        for i in words:
            l.append(i.split(separator))
        
        # flattened = [item for sublist in nested_list for item in sublist]

        m=[m for sub in l for m in sub]
        return list(filter(None,m))