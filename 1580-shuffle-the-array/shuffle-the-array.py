class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n=len(nums)//2
        # l1=nums[:n]
        # l2=nums[n:]
        # l3=[]
        # for i in range(n):
        #     l3.append(l1[i])
        #     l3.append(l2[i])
        # return l3
        l=[]
        for i in range(n):
            l.append(nums[i])
            l.append(nums[i+n])
        return l
