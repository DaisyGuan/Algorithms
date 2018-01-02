import collections

def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    return not collections.Counter(ransomNote) - collections.Counter(magazine)

print collections.Counter('ab') -collections.Counter('acb')
print canConstruct('ab','acb')
