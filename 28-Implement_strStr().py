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


    # KMP algorithm
    def getPrefix(self, pattern):
        # arr is pattern
        size = len(pattern)
        if size == 1:
            return [-1]
        len_prefix = 0
        i = 1
        prefix_table = [0]*size
        while i < size:
            if pattern[i] == pattern[len_prefix]:
                len_prefix += 1
                prefix_table[i] = len_prefix
                i += 1
            else:
                if len_prefix > 0:
                    len_prefix = prefix_table[len_prefix-1]
                else:
                    prefix_table[i] = len_prefix
                    i += 1
        prefix_table.pop()
        prefix_table.insert(0, -1)

        return prefix_table

    def kmpSearch(self, haystack, needle):
        len1 = len(haystack)
        len2 = len(needle)
        if len2 == 0:
            return 0
        prefix_table = self.getPrefix(needle)
        i = 0
        j = 0

        while j < len1:
            if i == len2 - 1 and needle[i] == haystack[j]:
                return j - i
            if needle[i] == haystack[j]:
                i += 1
                j += 1
            else:
                i = prefix_table[i]
                if i == -1:
                    i += 1
                    j += 1
        return -1




s = Solution()
print (s.kmpSearch("mississippi","a"))