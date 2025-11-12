class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        stack = []
        mx = 1
        for i in nums:
            if stack and stack[-1] >= i:
                mx = max(mx,len(stack))
                stack = []
            stack.append(i)

        mx = max(mx,len(stack))        
        return mx



