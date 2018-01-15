class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        places = []
        for p in path.split("/"):
            if p != "." and p !="":
                print p
                places.append(p)
        print places
        stack = []
        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)

result = Solution().simplifyPath("/a/./b/../../c/")
print result
