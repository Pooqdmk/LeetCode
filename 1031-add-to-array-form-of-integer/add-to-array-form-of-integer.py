import sys
sys.set_int_max_str_digits(20000)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=''
        for i in num:
            s+=str(i)
        a=str(int(s)+k)
        l=[]
        for i in a:
            l.append(int(i))
        return l
        