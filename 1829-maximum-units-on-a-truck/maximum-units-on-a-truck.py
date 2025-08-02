class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        l=sorted(boxTypes,key=lambda x:x[1],reverse=True)
        cnt=0
        for i in l:
            cnt+=(min(truckSize,i[0]))*i[1]
            truckSize-=min(truckSize,i[0])
            if truckSize == 0:
                break
        return cnt