class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n=len(arr)
        for i in range(n-m+1):
            pattern=arr[i:i+m]
            p=pattern*k
            
            # if ''.join([str(i) for i in p]) in ''.join([str(i) for i in arr]):
            #     return True

            for j in range(0,n-len(p)+1):
                if arr[j:j+len(p)] == p:
                    return True

        return False
