class Solution:
    def findFinalValue(self, nums: List[int], o: int) -> int:
        nums.sort()
        for i in nums:
            if i == o:
                o*=2
        return o

