_trie = lambda: collections.defaultdict(_trie)
INFO, END = True, False

class ShortList(list):
    def append(self, val):
        for i, (nt, s) in enumerate(self):
            if s == val[1]:
                self[i] = val
                break
        else:
            list.append(self, val)

        self.sort()
        if len(self) > 3:
            self.pop()

class AutocompleteSystem(object):

    def __init__(self, sentences, counts):
        self.curnode = self.trie = _trie()
        self.sentence_to_count = collections.Counter()
        self.search = ''

        for sentence, count in zip(sentences, counts):
            self.add(sentence, count)

    def add(self, sentence, count):
        self.sentence_to_count[sentence] = count
        cur = self.trie
        self._add_info(cur, sentence, count)
        for letter in sentence:
            cur = cur[letter]
            self._add_info(cur, sentence, count)
        cur[END] = sentence

    def _add_info(self, node, sentence, count):
        if INFO not in node:
            node[INFO] = ShortList()
        node[INFO].append((-count, sentence))

    def input(self, c):
        if c != '#':
            self.search += c
            if self.curnode is None:
                return []
            if c not in self.curnode:
                self.curnode = None
                return []

            self.curnode = self.curnode[c]
            return [s for nt, s in self.curnode[INFO]]
        else:
            self.sentence_to_count[self.search] += 1
            self.add(self.search, self.sentence_to_count[self.search])
            self.search = ''
            self.curnode = self.trie
            return []

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
