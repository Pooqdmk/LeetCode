class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        mx=-1
        while left<right:
            mx=max(mx,min(height[left],height[right])*(right-left))
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return mx