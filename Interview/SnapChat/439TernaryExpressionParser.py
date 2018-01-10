def parseTernary(self, expression):
        # begin with the last question.
        idx = []
        for i in xrange(len(expression)):
            if expression[i] == "?": idx += i,
        while len(expression) != 1:
            j = idx.pop()
            tmp = expression[j+1] if expression[j-1] == 'T' else expression[j+3]
            expression = expression[:j-1] + tmp + expression[j+4:]

        return expression


class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        expr = list(expression)
        while len(stack) > 1 or expr:
            tail = stack[-5:]
            if len(tail) == 5 and tail[3] == '?' and tail[1] == ':':
                tail = tail[2] if tail[4] == 'T' else tail[0]
                stack = stack[:-5] + [tail]
            else:
                stack.append(expr.pop())
        return stack[0] if stack else None

"""
Given a string representing arbitrarily nested ternary expressions, calculate the result of the expression. You can always assume that the given expression is valid and only consists of digits 0-9, ?, :, T and F (T and F represent True and False respectively).

Note:

The length of the given string is ≤ 10000.
Each number will contain only one digit.
The conditional expressions group right-to-left (as usual in most languages).
The condition will always be either T or F. That is, the condition will never be a digit.
The result of the expression will always evaluate to either a digit 0-9, T or F.

"""
