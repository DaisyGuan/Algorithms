# Complete the function below.


def  count_palindromes(S):
    def isPalindromes(s):
        if len(s)!=0 and s == s[::-1]:
            return True
        else:
            return False
    #print isPalindromes('AB')

    count = 0
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            if isPalindromes(S[i:j]):
                count += 1
            else:
                continue

    return count




print count_palindromes('ABA')
print 'ABA'
reversed('ABA')
