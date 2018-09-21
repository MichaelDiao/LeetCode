# coding:utf-8


# 解法1：暴力法
# 时间复杂度：O(n^3)
def force(s, nums):
    if len(nums) == 0:
        return 0
    mysum = 0
    minlen = len(nums)+1

    for i in range(1, len(nums)+1):# i means subarray length
        for j in range(len(nums)-i+1):# j means index in array
            for k in range(i):# k means index in subarray
                mysum += nums[j+k]
            if mysum >= s:
                if minlen > i:
                    minlen = i
            mysum = 0
    if minlen == len(nums)+1:
        return 0
    else:
        return minlen


# 解法2：暴力法优化
# 时间复杂度：O(n^2)
def forceOptimization1(s, nums):
    length = len(nums)
    if length == 0:
        return 0
    mySum = [0 for x in range(length+2)]
    for i in range(1, length+1):
        mySum[i] = mySum[i-1]+nums[i-1]

    ans = length + 1
    for l in range(length):
        for r in range(l, length):
            if mySum[r+1] - mySum[l] >= s:
                if ans > r-l+1:
                    ans = r-l+1
    if ans == length + 1:
        return 0
    else:
        return ans


# 解法3：滑动窗口
# 时间复杂度：O(n)
def slideWindow(s, nums):
    length = len(nums)
    minlen = length+1
    i = 0
    j = -1 # nums[i,j]为滑动窗口
    subsum = 0
    while i < length:
        if j + 1 < length and subsum <= s:
            j += 1
            subsum += nums[j]
        else:
            subsum -= nums[i]
            i += 1
        if subsum >= s:
            if minlen > j - i + 1:
                minlen = j - i + 1

    if minlen == length + 1:
        return 0
    else:
        return minlen


# 解法4：滑动窗口之2
# 时间复杂度：O(n)
def minSubArrayLen( s, nums):
    i = 0
    j = 0  # [i, j) null at start
    n = len(nums)
    tsum = 0
    while tsum < s:
        if j == n:
            return 0
        tsum += nums[j]
        j += 1
    while 1:
        tsum -= nums[i]  # [i, j) -> [i+1, j) try to be short
        i += 1
        if tsum < s:
            if j < n:
                tsum += nums[j]  # [i+1, j) -> [i+1, j+1)
                j += 1
            else:
                return j - i + 1  # j-(i-1)


def main():
    arr = [1, 2, 3, 4, 5, 15]
    print slideWindow(15, arr)


main()
