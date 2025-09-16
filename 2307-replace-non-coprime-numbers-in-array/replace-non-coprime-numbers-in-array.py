class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
        stack = []
        
        for i in nums:
            stack.append(i)
            while len(stack) > 1 and gcd(stack[-1],stack[-2]) != 1:
                v=stack.pop()
                u=stack.pop()
                stack.append(lcm(v,u))
                  
        return stack