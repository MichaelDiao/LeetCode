class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        len1 = len(s)
        i = 0
        index = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        while i < len1:
            if i+1 < len1 and index[s[i]] < index[s[i+1]]:
                res += index[s[i+1]] - index[s[i]]
                i += 2
            else:
                res += index[s[i]]
                i += 1
        return res

    def romanToInt2(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        previous = float('Inf')

        for i in s:
            current = dict[i]
            if previous < current:
                sum -= 2 * previous
            sum += current
            previous = current

        return sum

s = Solution()
print(s.romanToInt2("IXCM"))

