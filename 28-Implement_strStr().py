class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        len1 = len(haystack)
        len2 = len(needle)
        i = 0
        res = 0
        j = 0
        breakFlag = False
        while j < len1:
            if haystack[j] == needle[i]:
                res = j
                for k in xrange(i+1, len2):
                    j += 1
                    if j < len1:
                        if haystack[j] != needle[k]:
                            breakFlag = True
                            break
                    else:
                        return -1
                if not breakFlag:
                    return res
                else:
                    breakFlag = False
                    j = res + 1
            else:
                j += 1
        return -1

    def strStr2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not (needle in haystack):
            return -1
        if needle == "":
            return 0

        len1 = len(needle)
        for i in xrange(len(haystack)- len1 + 1):
            if haystack[i:i+len1] == needle:
                return i

s = Solution()
print (s.strStr("mississippi", "issip"))