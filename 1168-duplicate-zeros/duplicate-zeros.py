class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        cnt=arr.count(0)
        i=0
        while i < n:
            if arr[i]==0:
                arr.insert(i+1,0)
                i+=2
            else:
                i+=1

        while len(arr)>n:
            arr.pop()

        return arr