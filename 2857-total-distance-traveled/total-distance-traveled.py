class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        dist=0
        while mainTank>=5 and additionalTank>=1:
            mainTank-=5
            additionalTank-=1
            mainTank+=1
            dist+=50
            
        dist+=mainTank*10
        return dist