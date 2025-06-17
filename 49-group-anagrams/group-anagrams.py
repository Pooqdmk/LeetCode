class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n=len(strs)
        
        d=defaultdict(list)
        for i in strs:
            key=tuple(sorted(i))
            d[key].append(i)
            # if Counter(i) in d:
            #     d[Counter(i)].append()

        return list(d.values())