class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        s=sorted(nums)
        if nums == s:
            return 0
        n=len(nums)
        cnt,c=0,0
        while True:
            c+=1
            res=[0]*n
            for i in range(n):
                res[(i+1)%n]=nums[i]
            cnt+=1
            if res == s:
                return cnt
            nums=res
            if c > n:
                break
        return -1



                