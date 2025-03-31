class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d=Counter(arr1)
        a=[]
        for i in arr2:
            while d[i]>0:
                a.append(i)
                d[i]-=1
        r=sorted([i for i in arr1 if i not in arr2])
        a.extend(r)
        return a
        