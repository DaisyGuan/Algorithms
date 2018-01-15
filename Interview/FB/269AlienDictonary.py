class Solution(object):
    def alienOrder(self, words):
        less = []
        for pair in zip(words, words[1:]):
            #print pair
            for a, b in zip(*pair):
                #print a,b
                if a != b:
                    less += a + b,
                    break
        #print less
        #less = ['tf', 'we', 'rt', 'er']
        #print zip(*less)
        chars = set(''.join(words))
        #print chars
        order = []
        while less:
            free = chars - set(zip(*less)[1])
            print free
            if not free:
                return ''
            order += free
            less = filter(free.isdisjoint, less)
            print less
            chars -= free
        return ''.join(order + list(chars))

result = Solution().alienOrder([ "wrt","wrf","er","ett","rftt"])
print result
"""
x = [1,2,3]
y = [4,5,6]
zipped = zip(x,y)
unzipped_x, unzipped_y = zip(*zipped)
unzipped_x
    Out[30]: (1, 2, 3)
unzipped_y
    Out[31]: (4, 5, 6)
"""
