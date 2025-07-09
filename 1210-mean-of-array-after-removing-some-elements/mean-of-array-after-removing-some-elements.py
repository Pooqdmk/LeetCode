class Solution:
    def trimMean(self, arr: List[int]) -> float:
        k=int(.05*len(arr))
        arr.sort()
        return (sum(arr[k:-k]))/(len(arr)-2*k)