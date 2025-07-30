class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        while k>0:
            mx=max(gifts)
            index=gifts.index(mx)
            gifts[index]=floor(math.sqrt(mx))
            k-=1

        return sum(gifts)