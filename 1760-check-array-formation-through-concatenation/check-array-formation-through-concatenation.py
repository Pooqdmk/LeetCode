class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n=len(pieces)
        res=[]

        i=0
        while i < len(arr):
            found=False
            for j in pieces:
                if arr[i] in j:
                    found=True
                    res+=j
                    i+=len(j)
                    break
            if not found:
                return False
                

        return res == arr
        