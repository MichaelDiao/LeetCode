class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        len1 = len(nums)
        for i in range(len1):
            if nums[i] in dic.keys():
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]
        for i in range(1, len1):
            an = target - nums[i-1]
            if an in dic.keys():
                for j in range(len(dic[an])):
                    if dic[an][j] > i-1:
                        return [i-1, dic[an][j]]
        return None


    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len1 = len(nums)
        if len1 < 2:
            return None
        dic = {}
        for i in range(len1):
            if nums[i] in dic.keys():
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i
        return None

    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}

        for index, value in enumerate(nums):
            hash_map[value] = index
        print(hash_map)
        for index1, value in enumerate(nums):
            if target - value in hash_map:
                index2 = hash_map[target - value]

                if index1 != index2:
                    return [index1, index2]


nums1 = [2, 7, 11, 15, 7]
target1 = 14
s = Solution()
res = s.twoSum3(nums1, target1)
print(res)