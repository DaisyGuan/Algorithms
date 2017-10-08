def contkarr(A,k):
    maxSum = 0
    currSum = sum(A[0:k+1])
    for i in range(1,len(A)-k):
        currSum = currSum - A[i] + A[i+k]
        maxSum=max(maxSum, currSum)
    return maxSum

print contkarr([1,2,3,4,5,1,100], 4)
