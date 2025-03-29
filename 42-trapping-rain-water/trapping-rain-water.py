class Solution:
    def trap(self, height: List[int]) -> int:
        # cnt=0
        # for i in range(1,len(height)-1):
        #     cnt+=abs(height[i]-min(height[i-1],height[i+1]))
        # return cnt
        n=len(height)
        left=[0]*n
        left[0]=height[0]
        for i in range(1,n):
            left[i]=max(left[i-1],height[i])
        right=[0]*n
        right[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],height[i])

        cnt=0
        for i in range(n):
            cnt+=min(left[i],right[i])-height[i]
        return cnt