
def reverse( x):
    sign = cmp(x, 0)
    print sign
    r = sign*x
    r = int(`r`[::-1])#have question here
    if r < 2 ** 31:
        return sign*r
    else:
        return 0


print reverse(-321)
