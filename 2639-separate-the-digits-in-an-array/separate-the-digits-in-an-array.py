class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # res=[]

        # for i in nums:
        #     r=[]
        #     while i>0:
        #         r.append(i%10)
        #         i//=10
        #     res.append(r[::-1])
        # return sum(res,[])
        return [int(j) for i in nums for j in str(i)]