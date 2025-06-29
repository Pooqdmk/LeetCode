class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n=len(password)
        if n < 8:
            return False
        if password[0] == password[1]:
            return False

        l,u,d,s=0,0,0,0
        for i in range (1,n):
            if password[i] == password[i-1]:
                return False

            if password[i].islower():
                l+=1
            elif password[i].isupper():
                u+=1
            elif password[i].isdigit():
                d+=1
            else:
                s+=1
            
        if password[0].isalpha():
            if password[0].islower():
                l+=1
            else:
                u+=1
        elif password[0].isdigit():
            d+=1
        else:
            s+=1

        if l >=1 and u>=1 and d>=1 and s>=1:
            return True
        
        return False
