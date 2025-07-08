class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1,i1,r2,i2=0,0,0,0
        for i in range(len(num1)):
            if num1[i] == '+':
                r1=int(num1[:i])
                i1=int(num1[i+1:-1])
                break
        for i in range(len(num2)):
            if num2[i] == '+':
                r2=int(num2[:i])
                i2=int(num2[i+1:-1])
                break
        real = r1*r2 + i1*i2*-1
        img =(r1*i2 + r2*i1)
        return str(real) + '+' + str(img)+'i'
        