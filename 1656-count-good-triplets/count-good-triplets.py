class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # cnt=0
        # for i in range(len(arr)-2):
        #     for j in range(i+1,len(arr)-1):
        #         if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[j+1])<=b and abs(arr[i]-arr[j+1])<=c:
        #             cnt+=1
        # return cnt

        cnt=0
        n=len(arr)
        for i in range(n-2):
            for j in range(i+1,n-1):
                if abs(arr[i]-arr[j])<=a:
                    for k in range(j+1,n):
                        if abs(arr[j]-arr[k])<=b and abs(arr[k]-arr[i])<=c:
                            cnt+=1
        return cnt