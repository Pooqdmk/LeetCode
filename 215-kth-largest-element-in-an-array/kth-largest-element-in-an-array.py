class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # li={}
        # n=len(nums)
        # for i in range(n):
        #     cnt=0
        #     for j in range(n):
        #         if nums[i]<nums[j]:
        #             cnt+=1
        #     li[nums[i]]=cnt
        # for key,val in li.items():
        #     if val==k-1:
        #         return key
        return heapq.nlargest(k,nums)[-1]