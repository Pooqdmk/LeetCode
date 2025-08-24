class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        res=[]

        left,right = 0,n-1

        while left <= right:
            mid=(left+right)//2

            if x <= arr[mid]:
                right=mid-1
            else:
                left=mid+1
        
        l,r=left-1,left

        while k>0:

            if l<0:
                res.append(arr[r])
                r+=1
            elif r>=n:
                res.append(arr[l])
                l-=1

            else:
                if abs(arr[l]-x) <= abs(arr[r]-x):
                    res.append(arr[l])
                    l-=1
                else:
                    res.append(arr[r])
                    r+=1

            k-=1
        return sorted(res)




        

        

        
        