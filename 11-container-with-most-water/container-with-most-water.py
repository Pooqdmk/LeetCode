class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        mx = 0
        while l < r:
            mn = min(height[l],height[r])
            mx = max(mx, mn*(r-l))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return mx
