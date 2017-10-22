def titleToNumber(s):
    res = 0
    for i in s:
        res = 26*res + int(i,36) -9
    return res

print titleToNumber('AB')
print int('A',36)
print int('14',5)
