import collections
class Solution(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)

    def add(self, word):
        if word:
            self.word_dict[len(word)].append(word)
    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            for i, char in enumerate(word):
                if char != v[i] and char != '.':
                    break
            else:
                return True
        return False

"""
for-if-else
for xxx:
   if condition exist:
       do sth
       break
else:(condition not found)
    return sth

"""
A = collections.defaultdict(list)
A[2].append('haha')
print A
