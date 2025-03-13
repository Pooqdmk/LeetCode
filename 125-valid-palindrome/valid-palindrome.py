class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=""
        for i in s:
            if i.isalnum():
                n=n+i
        
        n=n.lower()
        if n==n[::-1]:
            return True
        else:
            return False