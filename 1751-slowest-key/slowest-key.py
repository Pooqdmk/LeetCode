class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        releaseTimes.insert(0,0)
        diff=0
        for i in range(1,len(releaseTimes)):
            d=releaseTimes[i]-releaseTimes[i-1]
            if(diff<d):
                diff=d
                key=keysPressed[i-1]
            elif diff==d:
                if key<keysPressed[i-1]:
                    key=keysPressed[i-1]
        return key