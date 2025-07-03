class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res=[-1]*(len(arr)+1)
        
        for i in range(len(arr)-1,-1,-1):
            mx=max(arr[i],res[i+1])
            res[i] = mx

        return res[1:]
            