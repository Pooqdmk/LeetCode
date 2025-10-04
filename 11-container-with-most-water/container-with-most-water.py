class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right =0,len(height)-1
        mx = -1
        while left < right:
            mx = max(mx, min(height[left],height[right]) * (right - left))
            if height[right] > height[left]:
                left+=1
            else:
                right-=1
        return mx
            
                 
