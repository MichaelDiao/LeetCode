# coding:utf-8
import time

# 解法1：暴力解法，超时
def forceTwoSum(arr, target):
    length = len(arr)
    for k in range(length):
        sum_ = arr[k]
        for h in range(k+1, length):
            sum_ += arr[h]
            if sum_ != target:
                sum_ = arr[k]
            else:
                return k, h
    return -1, -1


# 解法2：二分搜索
def binarySearch(arr, target):
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = (r+l)/2
        if arr[mid] > target:
            r = mid-1
        elif arr[mid] < target:
            l = mid+1
        else:
            return mid
    return -1


def binaryTwoSum(arr, target):
    for i in range(len(arr)):
        j = binarySearch(arr[i+1:], target-arr[i])
        if j != -1:
            return i+1, j+i+2
    return -1, -1


# 解法3：对撞索引法
def twoSum3(arr, target):
    i = 0
    j = len(arr)-1
    while i < j:
        su = arr[i] + arr[j]
        if su > target:
            j -= 1
        elif su < target:
            i += 1
        else:
            return i + 1, j + 1
    return -1, -1

def main():
    arr = []
    for k in range(13010):
        arr.append(0)
    arr.append(2)
    arr.append(3)
    for k in range(13008):
        arr.append(9)

    st = time.clock()
    i, j = twoSum3(arr, 5)
    # i, j = forceTwoSum(arr, 9)
    end = time.clock()

    print(i, j)
    print(end-st)


# run test
main()



