class Solution(object):
    def addBinary(self,a,b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #bin is already str
        return bin(int(a,2)+int(b,2))[2:]

    #recursive
    def addBinary2(self, a, b):
            if len(a)==0:
                return b
            if len(b)==0:
                return a

            if a[-1] == '1' and b[-1] == '1':
                return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
            if a[-1] == '0' and b[-1] == '0':
                return self.addBinary(a[0:-1],b[0:-1])+'0'
            else:
                return self.addBinary(a[0:-1],b[0:-1])+'1'

result = Solution()
re = result.addBinary('1','100')
print re
print bin(int("11",2))
