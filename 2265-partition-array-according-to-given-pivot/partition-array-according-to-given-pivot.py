class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        great = []
        cnt = 0
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                great.append(i)
            else:
                cnt+=1
        return less + [pivot]*cnt + great