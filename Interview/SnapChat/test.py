import sys
print sys.maxint
import math

#print 10/3
#print 10//3

dic = {"a": [1,2,3,4,5], "b" :[1], "c" : [5,6,7,3,3,45,4,56,2,5,4,32]}
kee = min(dic.keys(), key = lambda x: len(dic[x]))
#print kee

print math.factorial(4)
print [1, -1] * 5
