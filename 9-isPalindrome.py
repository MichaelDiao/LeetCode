class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return True if str(x) == str(x)[::-1] else False


    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        i = 0
        while x > i:
            i = i * 10 + x % 10
            x /= 10
        return x == i or x == i / 10


