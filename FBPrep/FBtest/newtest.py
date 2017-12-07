L = ['123','45']
#print zip(*L)

x = [1,2,3]
y = [4,5,6]
zipped = zip(x,y)
print zipped
a, b = zip(*zipped)
print list(a)
print b
