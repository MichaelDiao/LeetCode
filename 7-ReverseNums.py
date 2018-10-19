class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            str_x = str(-x)
            str_x = str_x[::-1]
            if int(str_x) > 2**31:
                return 0
            else:
                return -int(str_x)
        else:
            str_x = str(x)
            str_x = str_x[::-1]
            if int(str_x) > 2**31-1:
                return 0
            else:
                return int(str_x)


s = Solution()
res = s.reverse(-1230)
print(res)