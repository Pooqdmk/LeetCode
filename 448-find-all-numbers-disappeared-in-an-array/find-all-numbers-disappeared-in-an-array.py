class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=[]
        # for i in range(1,len(nums)+1):
        #     if i not in nums:
        #         l.append(i)

        # d=Counter(nums)
        s=set(nums)
        n=len(nums)
        for i in range(1,n+1):
            if i not in s:
                l.append(i)

        return l
