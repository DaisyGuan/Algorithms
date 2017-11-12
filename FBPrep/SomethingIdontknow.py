#173BST Iterator
#Implement an iterator over a binary search tree (BST).
#Your iterator will be initialized with the root node of a BST.
#Calling next() will return the next smallest number in the BST.
#Note: next() and hasNext() should run in average O(1) time and uses O(h) memory,
#where h is the height of the tree.
def __init__(self, root):
    self.stack = []
    while root:
        self.stack.append(root)
        root = root.left

# @return a boolean, whether we have a next smallest number
def hasNext(self):
    return len(self.stack) > 0

# @return an integer, the next smallest number
def next(self):
    node = self.stack.pop()
    x = node.right
    while x:
        self.stack.append(x)
        x = x.left
    return node.val

#56 Merge Intervals
def merge(self, intervals):
    lt = []
    for i in sorted(intervals, key=lambda i: i.start):#use start time to sort!!
        if lt and i.start <= lt[-1].end:
            lt[-1].end = max(lt[-1].end, i.end)
        else:
            lt.append(i)
    return lt

#211 Add and Search Word- Data Structure Design
class WordDictionary(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)


    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False

#208 Implement Trie
class TrieNode:
# Initialize your data structure here.
def __init__(self):
    self.children = collections.defaultdict(TrieNode)
    self.is_word = False

class Trie:

def __init__(self):
    self.root = TrieNode()

def insert(self, word):
    current = self.root
    for letter in word:
        current = current.children[letter]
    current.is_word = True

def search(self, word):
    current = self.root
    for letter in word:
        current = current.children.get(letter)
        if current is None:
            return False
    return current.is_word

def startsWith(self, prefix):
    current = self.root
    for letter in prefix:
        current = current.children.get(letter)
        if current is None:
            return False
    return True

#161 One Edit Distance
def editDistance(self,s,t):
    for i in range(min(len(s),len(t))):
        ...

#341 Flatten Nested List iterator
#670 Maximum Swap
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num))
        left, right = 0, 0
        max_idx = len(digits)-1
        for i in reversed(xrange(len(digits))):
            if digits[i] > digits[max_idx]:
                max_idx = i
            elif digits[max_idx] > digits[i]:
                left, right = i, max_idx
        digits[left], digits[right] = digits[right], digits[left]
        return int("".join(digits))
#133Clone an undirected graph.
#Each node in the graph contains a label and a list of its neighbors.
#33 Rotate
#494 target sum
#At first I just remember the current index and current target, and for each index,
#either subtract the nums[i] from S or add it to S. But this got TLE,
#them I came up with this solution. Just store the intermediate result with (index, s).
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def findTarget(i, s):
            if (i, s) not in cache:
                r = 0
                if i == len(nums):
                    if s == 0:
                        r = 1
                else:
                    r = findTarget(i+1, s-nums[i]) + findTarget(i+1, s+nums[i])
                cache[(i, s)] = r
            return cache[(i, s)]

        cache = {}
        return findTarget(0, S)
#productofArrayexpself: left and right parts
#523ContiSubarraySum
class Solution(object):
    def checkSubarraySum(self, nums, k):


        if k == 0:
            # if two continuous zeros in nums, return True
            # time O(n)
            for i in range(0, len(nums) - 1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False

        k = abs(k)
        if len(nums) >= k * 2:
            return True

        #if n >= 2k: return True
        #if n < 2k:  time O(n) is O(k)

        sum = [0]
        for x in nums:
            sum.append((sum[-1] + x) % k)

        Dict = {}
        for i in range(0, len(sum)):
            if Dict.has_key(sum[i]):
                if i - Dict[sum[i]] > 1:
                    return True
            else:
                Dict[sum[i]] = i

        return False

#Random Pick index
class Solution(object):

    def __init__(self, nums):
        self.nums = nums


    def pick(self, target):
        return random.choice([k for k, v in enumerate(self.nums) if v == target])

#2 zhong
def __init__(self, nums):
    self.nums = nums

def pick(self, target):
    res = None
    count = 0
    for i, x in enumerate(self.nums):
        if x == target:
            count += 1
            chance = random.randint(1, count)
            if chance == count:
                res = i
    return res
