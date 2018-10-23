class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        len1 = len(strs)
        if len1 == 0:
            return ""
        j = 0
        res = {}
        shortLen = float("Inf")
        for i in xrange(len1):
            len2 = len(strs[i])
            if len2 == 0:
                return ""
            if shortLen > len2:
                shortLen = len2

        while j < shortLen:
            tmp = strs[0][j]
            for i in xrange(1, len1):
                if strs[i][j] != tmp:
                    return "" if j == 0 else strs[0][:j]
            j += 1
        return strs[0][:shortLen]


s = Solution()
print(s.longestCommonPrefix([]))
print(s.longestCommonPrefix(["flower", "flow", "cart"]))

