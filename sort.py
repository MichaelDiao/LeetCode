import time
import random as rd


def sort(arr):
    zero = -1
    two = len(arr)
    i = 0
    while i < two:
        if arr[i] == 2:
            two -= 1
            if two == i:
                i += 1
                continue
            else:
                temp = arr[i]
                arr[i] = arr[two]
                arr[two] = temp
        elif arr[i] == 0:
            zero += 1
            if zero == i:
                i+=1
                continue
            else:
                try:
                    temp = arr[i]
                    arr[i] = arr[zero]
                    arr[zero] = temp
                    i += 1
                except Exception, msg:
                    print(msg)
                    while 1:
                        hh = 0
        else:
            i += 1
    return arr




arr = []
for j in range(100):
    arr.append(rd.randint(0,2))
print(arr)
arr2 = arr
st = time.clock()
ans = sort(arr)
end = time.clock()
print(ans)
print(str(end-st))

