class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
        stack = []
        i=0
        while i < len(nums):
            stack.append(nums[i])
            while len(stack) > 1 and gcd(stack[-1],stack[-2]) != 1:
                v=stack.pop()
                u=stack.pop()
                stack.append(lcm(v,u))
                  
            i+=1
        return stack