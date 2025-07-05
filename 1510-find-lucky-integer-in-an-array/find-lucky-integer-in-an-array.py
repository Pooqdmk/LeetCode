class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d=Counter(arr)
        mx=-1
        for key,val in d.items():
            if key == val:
                mx=max(mx , key)
        return mx