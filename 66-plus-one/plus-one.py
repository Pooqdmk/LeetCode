class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num = num*10 + digits[i]
        
        num = num+1

        l = []
        while num > 0:
            l.append(num % 10)
            num//=10
        return l[::-1]


            
