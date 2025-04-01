class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        i=0
        l=len(arr)
        m=10**50
        li=[]
        while i<l-1:
            diff=abs(arr[i+1]-arr[i])
            if m>diff:
                m=diff
                li=[[arr[i],arr[i+1]]]
            elif m==diff:
                li.append([arr[i],arr[i+1]])
            i+=1
        return li

            

