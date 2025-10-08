class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []
        for i in spells:
            n=ceil(success/i)

            left,right =0,m
            first_idx = m
            while left < right:
                mid = (left + right)//2

                if potions[mid] < n:
                    left = mid+1
                else:
                    first_idx = mid
                    right=mid 
            
            res.append(m-first_idx)

        return res

            
