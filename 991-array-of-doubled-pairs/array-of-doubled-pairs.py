class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        d=Counter(arr)
        arr.sort(key=abs)

        for i in arr:
            if d[i] == 0:
                continue
            if d[2*i] == 0:
                return False
            d[i]-=1
            d[2*i]-=1
        return True
        
