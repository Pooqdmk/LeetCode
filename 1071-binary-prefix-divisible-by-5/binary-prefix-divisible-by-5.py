import sys
sys.set_int_max_str_digits(20000)
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # l=[]
        # s=''
        # for i in nums:
        #     s+=str(i)
        #     if int(s,2)%5==0:
        #         l.append(True)
        #     else:
        #         l.append(False)
        # return l

        l=[]
        k=0
        for i in nums:
            k=(k*2+i)%5
            l.append(k==0)
        return l