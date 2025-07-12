class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt=0
        for i in nums:
            # if len(str(i))%2==0:
            #     cnt+=1
            c=0
            while i>0:
                c+=1
                i//=10
            if c%2==0:
                cnt+=1
        return cnt