class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        clean = [nums[0]]

        for i in nums[1:]:
            if i != clean[-1]:
                clean.append(i)
        cnt=0
        for i in range(1,len(clean)-1):
            if (clean[i]>clean[i-1] and clean[i]>clean[i+1]) or (clean[i]<clean[i-1] and clean[i]<clean[i+1]):
                cnt+=1

        return cnt