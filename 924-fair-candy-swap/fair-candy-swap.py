class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a=sum(aliceSizes)
        b=sum(bobSizes)
        alice_gives=(a-b)//2
        setB=set(bobSizes)

        for i in aliceSizes:
            if i-alice_gives in setB:
                return [i,i-alice_gives]