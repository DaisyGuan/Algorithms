class Solution(object):
    def calculate(self, s):
        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                print signs
                total += signs.pop() * int(s[start:i])
                continue
            if c in '+-(':
                signs += signs[-1] * (1, -1)[c == '-'],
            elif c == ')':
                signs.pop()
            i += 1
        return total

    def calculate2(self, s):
    res, num, sign, stack = 0, 0, 1, [1]
    for i in s+"+":
        if i.isdigit():
            num = 10*num + int(i)
        elif i in "+-":
            res += num * sign * stack[-1]
            sign = 1 if i=="+" else -1
            num = 0
        elif i == "(":
            stack.append(sign * stack[-1])
            sign = 1
        elif i == ")":
            res += num * sign * stack[-1]
            num = 0
            stack.pop()
    return res

result = Solution().calculate(" 2-1 + 2 ")
print result
