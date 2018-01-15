class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        #first sorted the strs
        for w in sorted(strs):
            #let key be tuple of each str w, tuple: sequence of immutatable objects, parentheses
            #list is unhashable
            #can't use a list as the key in a dict,
            #since dict keys need to be immutable. Use a tuple instead.
            key = tuple(sorted(w))
            #update value according to different key, append new strs to the same key
            #instead of d[key], d.get(key,[]),It allows you to provide a default value if the key is missing
            d[key] = d.get(key,[]) + [w]
        return d.values()
        #return d's all values

#running time O(n)

result = Solution()
re = result.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
#print re
print sorted(["eat", "tea", "tan", "ate", "nat", "bat"])
print sorted('abdfasdf')
print tuple('abdfasdf')


"""
dictionary = {"message": "Hello, World!"}
data = dictionary.get("message", "")
print(data)  # Hello, World!
dict.get(key[, default])
"""
