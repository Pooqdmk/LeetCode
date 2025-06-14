class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        index=s.find('6')
        if index==-1:
            return num
        r=s[:index]+'9'+s[index+1:]

        return int(r)

        # return int(str.replace(index,'9'))