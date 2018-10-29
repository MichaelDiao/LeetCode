class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return None
        if n == 1:
            return "1"
        res = ""
        queue = [1]
        while n > 1:
            res = ""
            cur_num = queue[0]
            queue.pop(0)
            cnt = 1
            while len(queue) != 0:
                if cur_num == queue[0]:
                    queue.pop(0)
                    cnt += 1
                else:
                    res += (str(cnt) + str(cur_num))
                    cur_num = queue[0]
                    queue.pop(0)
                    cnt = 1
            res += (str(cnt) + str(cur_num))
            queue = list(res)
            n -= 1

        return res


s = Solution()
print (s.countAndSay(4))


