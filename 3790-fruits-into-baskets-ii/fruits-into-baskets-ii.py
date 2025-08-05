class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        cnt=0
        n=len(fruits)
        for i in range(n):
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j]:
                    del baskets[j]
                    cnt+=1
                    break
        return n-cnt
