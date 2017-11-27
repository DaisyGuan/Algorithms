class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        Square1 = abs(C-A) * abs(D-B)
        Square2 = abs(G-E) * abs(H-F)

        if (E >= C) or (A >= G) or (F >= D) or (H <= B):
            return Square1 + Square2
        else:
                xlist = [A,E,C,G]
                xlist.sort()
                ylist = [D,H,B,F]
                ylist.sort()
                Overlap = abs(xlist[2]-xlist[1])*abs(ylist[2]-ylist[1])

                return Square1 + Square2 - Overlap
        
