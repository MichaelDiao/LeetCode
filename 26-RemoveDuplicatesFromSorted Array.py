class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len1 = len(nums)
        if len1 < 2:
            return len1
        i = 0
        j = 1
        while j < len1:
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
                j += 1
        return i+1


    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        for i in xrange(len(nums)):
            if nums[j] != nums[i]:
                nums[j + 1] = nums[i]
                j += 1
        return j + 1


s = Solution()
print (s.removeDuplicates2([0,1,1,1,2,2,3,3,4]))