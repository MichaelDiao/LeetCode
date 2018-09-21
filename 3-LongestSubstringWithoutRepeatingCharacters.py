# coding:utf-8

import time


# 解法1：暴力方法
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)
# 用时60ms（leetcode平台测试结果）
def force(s):
    length = len(s)
    if length == 0:
        return 0
    if length == 1:
        return 1
    l = 0
    r = 1 # s[l,r]
    maxlen = 0
    while r < length:
        if s[r] in s[l:r]:
            while s[l] != s[r]:
                l += 1
            l += 1
        if maxlen < r - l + 1:
            maxlen = r - l + 1
        r += 1

    return maxlen


# 解法2：字典查询法
# 时间复杂度：O(n)
# 空间复杂度：O(1)
# 注意一点的是：在更新滑动窗口的左边界时，要注意判断已存在的重复值是否在左边界的右边，若在右边才可以将窗口右移，即左边界右移。
# 用时56ms（leetcode平台测试结果）
def lenthOfLongestSubstr(s):
    length = len(s)
    l = 0
    r = 0 # s[l,r]
    maxlen = 0
    pos = {}
    while r < length:
        c = s[r]
        if c in pos and pos[c] >= l:
            l = pos[c] + 1
        pos[c] = r
        n = r - l + 1
        if maxlen < n:
            maxlen = n
        r += 1
    return maxlen


# 解法3：ascii表查询法
# 时间复杂度：O(n)
# 空间复杂度：O(1)
# 生成固定长度的list，用[0]*256的方式速度比[0 for i in range(256)]快约10倍
# 用时52ms（leetcode平台测试结果）
def lenthOfLongestSubstr2(s):
    # s = time.clock()
    # asc = [0 for i in range(256)]
    # e = time.clock()
    # print e - s
    # s = time.clock()
    asc = [-1]*256
    # e = time.clock()
    # print e - s
    length = len(s)
    l = 0
    r = 0 # s[l,r]
    maxlen = 0
    while r < length:
        od = ord(s[r])
        fre = asc[od] # fre为s[r]的下标
        if fre >= l:
            l = fre + 1
        asc[od] = r
        n = r - l + 1
        if n > maxlen:
            maxlen = n
        r += 1
    return maxlen


def main():
    s = ["abba", "bbbbb", "pwwkew", "", " "]
    for c in s:
        # print c
        print lenthOfLongestSubstr2(c)


main()
