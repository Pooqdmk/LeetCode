class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s=math.sqrt(num)
        j=0
        for i in range(len(str(s))):
            if str(s)[i]=='.':
                j=i
                break
        if int(str(s)[j+1:])==0:
            return True
        else:
            return False
        # if int(s)!=int(str(s)[:j]):
        #     return False
        # else:
        #     return True
