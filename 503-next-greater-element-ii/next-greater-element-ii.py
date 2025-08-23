class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        for i in range(n):
            found=False
            for j in range(n):
                if nums[(j+i+1) % n] > nums[i]:
                    found=True
                    res.append(nums[(j+i+1)%n])
                    break
            if not found:
                res.append(-1)
        return res
