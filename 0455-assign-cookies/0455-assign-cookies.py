class Solution(object):
    def findContentChildren(self, g, s):
        i,j=0,0
        g.sort()
        s.sort()
        m=len(g) 
        n = len(s)
        while(i<m and j< n):
            if(s[j]>=g[i]):
                i = i+1
            j = j+1
        return i
        