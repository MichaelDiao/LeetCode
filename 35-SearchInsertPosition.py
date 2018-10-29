class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pos = -1
        len1 = len(nums)
        if nums[0] > target:
            return 0
        elif nums[len1-1] < target:
            return len1

        for i in xrange(len1):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                pos = i
            else:
                if i - pos == 1:
                    return i


    def searchInsert2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len1 = len(nums)
        if nums[0] > target:
            return 0
        elif nums[len1-1] < target:
            return len1
        l = 0
        r = len1 -1

        while l <= r:
            mid = (r + l)/2
            if nums[mid] == target or (nums[mid-1] < target and nums[mid] > target):
                return mid
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1





s = Solution()
print (s.searchInsert2([1, 3, 5, 6], 6))
