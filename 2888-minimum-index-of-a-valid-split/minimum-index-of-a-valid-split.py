class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        d=Counter(nums)
        freq=max(d.values())
        dom=next(key for key,val in d.items() if val==freq)

        l=0
        r=freq
        for i in range(len(nums)):
            if nums[i]==dom:
                l+=1
                r-=1
            if l*2>(i+1) and r*2>(len(nums)-(i+1)):
                return i
        return -1
        