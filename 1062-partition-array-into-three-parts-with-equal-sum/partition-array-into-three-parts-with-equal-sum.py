class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s=sum(arr)
        if s%3 != 0:
            return False
        d=s//3
        curr_sum=0
        cnt=0
        for i in range(len(arr)):
            curr_sum+=arr[i]
            if curr_sum == d:
                cnt+=1
                curr_sum=0
                if cnt == 2 and i<len(arr)-1:
                    return True

        return False
