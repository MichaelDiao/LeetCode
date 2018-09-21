# coding:utf-8


# 解法1：暴力法
# 时间复杂度：O(n)
# 空间复杂度：O(n)
def force(s):
    if s == '':
        return True
    s = s.lower()
    str2 = [i for i in s if 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57]
    if str2 != str2[::-1]:
        return False
    else:
        return True


def main():
    s = "A man, a plan, a canal: Panama"
    print force(s)


main()
