class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)
        if s%3 == 0:
            return s
        elif s%3 == 2:
            nums.sort()
            t = 0
            cnt = 0
            for i in nums:
                if i%3 == 2:
                    if cnt == 2:
                        return s-min(i,t)
                    return s-i
                elif i%3 == 1 and cnt < 2:
                    t+=i
                    cnt+=1
            return s-t if cnt == 2 else 0            
                            
        else:
            nums.sort()
            t = 0
            cnt = 0
            for i in nums:
                if i%3 == 1:
                    if cnt == 2:
                        return s-min(i,t)
                    return s-i
                elif i%3 == 2 and cnt < 2:
                    t+=i
                    cnt+=1
            return s-t if cnt == 2 else 0  
               



