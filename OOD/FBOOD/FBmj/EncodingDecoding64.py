#BASE64
import base64
encoded = base64.b64encode("absdsdfa")
#print encoded
data = base64.b64decode(encoded)
#print data
import binascii
#print binascii.b2a_base64('absdsdfa')
#Convert binary data to a line of ASCII characters in base64 coding.
#print binascii.a2b_base64('YWJzZHNkZmE=')
#Convert a block of base64 data back to binary and return the binary data. More than one line may be passed at a time.

import urllib2
def urlencode(s):
    return urllib2.quote(s)
def urldecode(s):
    return urllib2.unquote(s).decode('utf8')

result = urlencode('https://gist.github.com/renyi/ ')
#print result
#print urldecode(result)

#binary to hex
#print hex(int('10000011101000011010100010010111', 2))
#Hex to binary
#print bin(0x83a1a897)
print "absdsdfa".encode("base64")
print "YWJzZHNkZmE=".decode('base64')
print "https://gist.github.com/renyi/ ".encode('url')
#Perform hexbin4 binary-to-ASCII translation and return the resulting string.
#The argument should already be RLE-coded, and have a length divisible by 3 (except possibly the last fragment).
#print binascii.a2b_uu('0101110')
#Convert a single line of uuencoded data back to binary and return the binary data.
#Lines normally contain 45 (binary) bytes, except for the last line. Line data may be followed by whitespace.
#print binascii.b2a_uu('EQE')
