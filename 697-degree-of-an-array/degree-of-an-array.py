class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c=Counter(nums)
        # for key,val in c.items():
        m=max(c.values())
        l=[]
        for key,val in c.items():
            if val==m:
                l.append(key)
        min_len=10**8
        for i in l:
            min_len=min(min_len,(len(nums)-nums[::-1].index(i)-1) -nums.index(i)+1)
        return min_len
            