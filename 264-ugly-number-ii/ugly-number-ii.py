class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr = [1]
        i2,i3,i5 = 0,0,0
        for i in range(1,n):

            mn = min(arr[i2]*2,arr[i3]*3,arr[i5]*5)
            arr.append(mn)
            if mn == arr[i2]*2:
                i2+=1
            if mn == arr[i3]*3:
                i3+=1
            if mn == arr[i5]*5:
                i5+=1
        return arr[n-1]
            
            