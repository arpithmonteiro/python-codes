class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        org=str(x)
        return (org==org[::-1])
        # while(x>0):
        #     rem=x%10
        #     x=x/10
        #     rev=rev*10+rem
        
