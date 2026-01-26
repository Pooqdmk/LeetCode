class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        res = []
        mn = 10**60
        for i in range(len(arr)-1):
            diff = arr[i+1]-arr[i]
            if mn > diff:
                mn = diff
        for i in range(len(arr)-1):
            if mn == arr[i+1]-arr[i]:
                res.append([arr[i],arr[i+1]])
        return res
