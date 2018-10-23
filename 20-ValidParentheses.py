class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len1 = len(s)
        if len1 % 2 == 1:
            return False
        if len1 == 0:
            return True
        match = {'(': 1, ')': -1, '[': 2, ']': -2, '{': 3, '}': -3}
        li1 = list(s)
        li2 = [li1.pop()]
        while li1:
            if match[li1[-1]] + match[li2[-1]] == 0:
                li1.pop()
                li2.pop()
                if len(li2) == 0 and len(li1) != 0:
                    li2.append(li1.pop())
            else:
                li2.append(li1.pop())
        if li2:
            return False
        else:
            return True

    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        len1 = len(s)
        if len1 == 0:
            return True
        if len1 % 2 == 1:
            return False

        stack = []
        dic = {']': '[', ')': '(', '}': '{'}
        for i in s:
            if i not in dic.keys():
                stack.append(i)
            else:
                if stack and stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
        return not stack


s = Solution()
print (s.isValid2("(){{})[]{}"))
