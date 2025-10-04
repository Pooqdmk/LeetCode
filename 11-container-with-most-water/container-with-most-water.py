class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right =0,len(height)-1
        mx = -1
        while left < right:
            mn = min(height[left],height[right])
            mx = max(mx, mn * (right - left))
            if mn == height[left]:
                left+=1
            else:
                right-=1
        return mx
            
                 
