class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d=Counter(target)
        l=Counter(arr)

        for key,val in d.items():
            if l[key] and val == l[key]:
                continue
            else:
                return False
        return True