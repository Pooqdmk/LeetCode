class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e,o=[],[]
        for i in range(len(nums)):
            if i%2==0:
                e.append(nums[i])
            else:
                o.append(nums[i])

        e.sort()
        o.sort(reverse=True)
        j,k=0,0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=e[j]
                j+=1
            else:
                nums[i]=o[k]
                k+=1

        return nums






