class Solution(object):# may overflow
    def multiply1(self, num1, num2):
        return str(int(num1)*int(num2))

    # may overflow
        def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = 0
        for i, j in enumerate(num2[::-1]):
            temp = int(j) * (10 ** i)
            for x, y in enumerate(num1[::-1]):
                res += int(y) * (10**x) * temp

        return str(res)

    # No overflow
    def multiply2(self, num1, num2):
        res = [0] * (len(num1) + len(num2))
        for i in xrange(len(num1)-1, -1, -1):
            carry = 0
            for j in xrange(len(num2)-1, -1, -1):
                tmp = int(num1[i])*int(num2[j])+carry
                # take care of the order of the next two lines
                carry = (res[i+j+1] + tmp) // 10
                res[i+j+1] = (res[i+j+1] + tmp) % 10
                # or simply: carry, res[i+j+1] = divmod((res[i+j+1] + tmp), 10)
            res[i] += carry
        res = "".join(map(str, res))
        return '0' if not res.lstrip("0") else res.lstrip("0")



num1="12345"
for i, j in enumerate(num1):
    print i,j
