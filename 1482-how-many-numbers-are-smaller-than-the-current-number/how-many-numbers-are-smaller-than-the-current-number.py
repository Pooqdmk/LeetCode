class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num=sorted(nums)
        d={}
        for i in range(len(num)):
            cnt=0
            for j in range(0,i):
                if num[i]>num[j]:
                    cnt+=1
            d[num[i]]=cnt
        li=[]
        for i in nums:
            li.append(d[i])
        return li
