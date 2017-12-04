import base64
encoded = base64.b64encode("")
print encoded
data = base64.b64decode(encoded)
print data
s = 'haha/gdfsa/dfaf'
print s.split('/')

["X:Z;Y_","RtbB9G(P","On?>","{y,9f~wgL"]

import base64
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for s in strs:
            res += base64.b64encode(s) +'/'
        return res


    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        res = s.split('/')

        for i in range(len(res)):
            res[i] = base64.b64decode(res[i])
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
