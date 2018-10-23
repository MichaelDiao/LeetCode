class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        len1 = len(nums)
        if len1 == 0:
            return 0
        tmp = len1 - 1
        i = 0
        cnt = 0
        while i <= tmp:
            if nums[i] == val:
                while nums[tmp] == val and tmp > i:
                    tmp -= 1
                if tmp > i:
                    nums[i] = nums[tmp]
                    cnt += 1
                    tmp -= 1
            else:
                cnt += 1
            i += 1
        return cnt

    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        len1 = len(nums)
        if len1 == 0:
            return 0
        j = 0
        for i in xrange(len1):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j


s = Solution()
print (s.removeElement2([2], 2))


