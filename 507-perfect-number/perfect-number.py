class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # t=0
        s=set()
        for i in range(1,int(math.sqrt(num))+1):
            if num%i==0:
                s.add(i)
                s.add(num//i)

        if sum(s)-num==num:
            return True
        else:
            return False