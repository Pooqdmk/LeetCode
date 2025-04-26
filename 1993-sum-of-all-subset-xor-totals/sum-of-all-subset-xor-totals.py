class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # cnt=0
        # n=len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         xor=0
        #         for k in nums[i:j]:
        #             xor^=k
        #         cnt+=xor
        # return cnt
        l=[[]]
        cnt=0
        for i in nums:
            l+=[[i]+cur for cur in l]
            
        for j in l:
            xor=0
            for k in j:
                xor^=k
            cnt+=xor
        return cnt