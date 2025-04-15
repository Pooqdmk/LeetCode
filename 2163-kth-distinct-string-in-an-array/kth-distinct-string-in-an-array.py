class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d=Counter(arr)
        li=[]
        for i in arr:
            if d[i]==1:
                li.append(i)
        try:
            return li[k-1]
        except IndexError:
            return ""


