
def quickSort(arr, left, right):
    l = left
    r = right
    base = arr[l]
    while l < r:
        while l < r and arr[r] <= base:
            r -= 1
        while l < r and arr[l] >= base:
            l += 1
        if l < r:
            te = arr[r]
            arr[r] = arr[l]
            arr[l] = te
    arr[left] = arr[l]
    arr[l] = base
    return l


def solution1(arr, k):
    if len(arr) <= 0 or k <= 0 or len(arr) < k:
        return -1
    ans = 0
    left = 0
    right = len(arr)-1
    for i in range(len(arr)):
        if left >= right and left >= len(arr) and right <= 0:
            return -1
        ans = quickSort(arr, left, right)
        if ans == k-1:
            return arr[ans]
        elif ans > k-1:
            right = ans - 1
        else:
            left = ans + 1
        i+=1


arr = [4, 6, 2, 3, 1, 5, 7, 8]
for i in range(len(arr)):
    ans = solution1(arr, i+1)
    print(ans)